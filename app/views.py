from operator import ilshift
import os
from unicodedata import category

from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from django.urls import reverse_lazy
import email
import math
import base64
import requests
import random


from .utils import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from .forms import *
# from partner.partners.models import Partner
from django.contrib.auth import logout, authenticate, login
from django.core.files.storage import FileSystemStorage
from account.models import Account
from .forms import ProductCreateForm
from .models import Chat_room, Message
from datetime import datetime, date

from .forms import CustomUserChangeForm

# extra functions sector
content = {}

# upload images to hosting 
# takes (image as file, name of image) -> returns (link and prev name)
def upload_image(image, name):
    
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": '4d8bfed1807797ed805abf76382f3ed9',
        "image": base64.b64encode(image.read()),
        "name": name
    }

    res = requests.post(url, payload)
    link = res.text.split('thumb')[-1].split("delete")[0][3:-3].split(",")[-1].split('":"')[-1][:-1].replace('\\', '') 
    name = res.text.split('name":"')[-1].split('"')[0]
    return [link, name]

# get rundom amount of ids from sertain DB element
# takes (name of db sector, aount of items) -> returns (random ids as arr of arrs)
def random_DB_id(segment, amount):
    ev_id = [i.id for i in eval('segment.objects.all()')]
    size = amount if amount <= len(ev_id) else len(ev_id)
    id_arr, ret_arr = [], []
    while len(id_arr) != min(len(ev_id), amount):
        id_arr = [*set([ random.choice(ev_id) for i in range(size) ])]  
    for i in range(len(id_arr)):
        ret_arr.append(eval('segment.objects.filter(id = id_arr[i])'))
    return ret_arr


# error sector
# 400 error template
def pageNotAccess(request, exception):
    return render(request, 'errorPages/400.html')

# 403 error template
def pageMistakeServ(request, exception):
    return render(request, 'errorPages/403.html')

# 404 error template
def pageNotFound(request, exception):
    return render(request, 'errorPages/404.html')

# 500 error template
def pageNotRequest(request):
    return render(request, 'errorPages/500.html')

# admin sector
def admin_page(request):
    if request.user.is_authenticated and request.user.is_admin and request.user.is_staff and request.user.is_superuser :

        content['partners'] = BePartner.objects.all()
        if request.method == 'POST' and "deletePaartner" in request.POST:
            BePartner.objects.get(id=request.POST['deletePaartner']).delete()
            return HttpResponseRedirect('/admin')
        if request.method == 'POST' and "submitPaartner" in request.POST:
            part = BePartner.objects.get(id=request.POST['submitPaartner'])
            shop = Shop.objects.create()
            user = User.objects.get(email=part.email)
            shop.email = part.email
            shop.phone = part.phone
            shop.name = part.brand_name
            shop.save()

            user.is_partner = 1
            user.save()
            part.delete()
            return HttpResponseRedirect('/admin')
        return render(request, 'admin.html', content)

            
    else:
        return HttpResponseRedirect('/')



# enterance sector
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def login_page(request):
    form = SignUpForm(request.POST)
    content = {
        'form': form
    }
    # enterance request
    if request.method == 'POST' and 'btnform2' in request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        elif request.POST.get('password') != '':
            print('Try again! username or password is incorrect')
            content['errors'] = 'Try again! username or password is incorrect'
    # registration request
    elif request.method == 'POST' and 'btnform1' in request.POST:
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            username = email
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password, first_name=first_name)
            return redirect('/login/')
        else:
            print(form.errors)

    return render(request, 'signin.html', content)


# main page sector
def index_page(request):
    products = Product_creator.objects.all()
    content['products_start'] = [product for product in products[0:6]]
    content['products_bottom_1'] = [product for product in products[0:25]]

    shops = Shop.objects.all()

    content['shops'] = [shop for shop in shops[0:4]]

    if request.user.is_authenticated:
        # content['prom_shops'] =  [i for i in random_DB_id(Shop, 8)]
        # content['prom_items'] = [i for i in random_DB_id(Product_creator, 8)]
        return render(request, 'index.html', content)
    else:
        return render(request, 'index.html', content)


# user sector
def edit_profile(request):
    try:
        email = request.user
        person = Account.objects.get(email=email)
        if request.method == "POST":
            if request.FILES:


                file = request.FILES['profile_photo']
                filename = f"profile_{str(person.email)}"

                logoImageData = upload_image(file, filename)
                person.userImage = logoImageData[0]
                # shop.prevLogoImage = logoImageData[-1]

             
            if request.POST.get('first_name', None):
                person.first_name = request.POST['first_name']
            if request.POST.get('last_name', None):
                person.last_name = request.POST['last_name']
            if request.POST.get('phone', None):
                person.phone = request.POST['phone']
            if request.POST.get('city', None):
                person.city = request.POST['city']
            person.save()
            return HttpResponseRedirect("/edit/")
        else:
            content['user'] = person
            return render(request, "editProfile.html", content)

    except Account.DoesNotExist as e:
        raise Http404 from e

def forgot_password_page(request):
    return render(request, 'forgotPassword.html')


# user shop sector
def cart_page(request):
    user = request.user
    cart_items = Cart.objects.filter(id_user_buy = user)
    content['items'] = [i for i in cart_items]
    content['shops'] = set()
    for i in cart_items:
        content['shops'].add(i.brand)
        content['shops'] = set(content['shops'])
    content['sum'] = sum(int(i.price) for i in cart_items)
    content['randProducts'] = [i for i in random_DB_id(Product_creator, 3)]
    if request.method == 'POST' and 'payButton' in request.POST:
        products = Cart.objects.filter(id_user_buy = request.user)
        print(12312312312312312312312)
        return HttpResponseRedirect('/cart/')

    if request.method == 'POST' and 'decline' in request.POST:
        Cart.objects.filter(id = request.POST['decline']).delete()
        return HttpResponseRedirect('/cart/')

    return render(request, 'cart.html', content)


def orders_page(request):
    products = Orders.objects.filter(id_user_buy=request.user)
    content['shops'] = set()
    for i in products:
        if not i.is_incart:
            content['shops'].add(i.brand)
            content['shops'] = set(content['shops'])
    content['products'] = [{
                        'id':product.id,
                        'id_creator':product.id_creator,
                        'brand':product.brand,
                        'id_user_buy':product.id_user_buy,
                        'price':product.price,
                        'duration':product.duration,
                        'compound':product.compound,
                        'size':product.size,
                        'amount':product.amount,
                        'product_name':product.product_name,
                        'status':product.status,
                        'message':product.message,
                        'is_payed':product.is_payed,
                        'delivery_address':product.delivery_address,
                        'date_add':product.date_add,
                        'img':product.img,
                        'is_incart':product.is_incart,
                        } for product in products]
    

    if request.method == "POST" and "decline" in request.POST:
        Cart.objects.get(id=request.POST['decline']).delete()
        return HttpResponseRedirect('/orders/')

    return render(request, 'orders.html', content)



# partner sector
def becomeCreator_page(request):  # sourcery skip: low-code-quality
    user = Account.objects.get(email=request.user)
    shop = Shop.objects.get(email=request.user.email)

    # profile editing
    if request.method == 'POST' and "profile_saver1" in request.POST:  

        
        user.name_small = request.POST['name_small']
        user.nameFull = request.POST['nameFull']
        user.ogrn = request.POST['ogrn']
        user.inn = request.POST['inn']
        user.kpp = request.POST['kpp']
        user.street = request.POST['street']
        user.fiz_adress = request.POST['fiz_adress']
        user.city = request.POST['city']
        user.index = request.POST['index']
        user.payment_account = request.POST['payment_account']
        user.reg_form = request.POST['reg_form']
        user.bik = request.POST['bik']
        user.korr_check = request.POST['korr_check']
        user.save()
        return HttpResponseRedirect("/becomeCreator/")

    # profile editing
    if request.method == 'POST' and "profile_saver2" in request.POST: 

        shop.name = request.POST['name']
        shop.description = request.POST['description']
        shop.status = request.POST['status']
        shop.category = request.POST['chosenCategoties']


        if request.FILES:

            try:
                if request.FILES['logoImage']:

                    file = request.FILES['logoImage']
                    filename = f"prof_{str(shop.email)}"

                    logoImageData = upload_image(file, filename)
                    shop.logoImage = logoImageData[0]
                    # shop.prevLogoImage = logoImageData[-1]

                else:
                    pass
            except:
                pass

            try:
                    
                if request.FILES['bgImage']:

                    file = request.FILES['bgImage']
                    filename = f"bg_{str(shop.email)}"

                    logoImageData = upload_image(file, filename)
                    shop.bgImage = logoImageData[0]

                    # shop.prevLogoImage = logoImageData[-1]

                else:                        
                    pass
            except:
                pass


        shop.save()
        return HttpResponseRedirect("/becomeCreator/")

    # creating product
    if request.method == 'POST' and "product_creator" in request.POST:  
        product = Product_creator()

        if request.FILES:

            file1 = request.FILES['product_photo1']
            file2 = request.FILES['product_photo2']
            file3 = request.FILES['product_photo3']

            filename1 = f'product_photo1_{str(request.user.email)}'
            filename2 = f'product_photo2_{str(request.user.email)}'
            filename3 = f'product_photo3_{str(request.user.email)}'

            logoImageData1 = upload_image(file1, filename1)
            logoImageData2 = upload_image(file2, filename2)
            logoImageData3 = upload_image(file3, filename3)
    
            product.picture1 = logoImageData1[0]
            product.picture2 = logoImageData2[0]
            product.picture3 = logoImageData3[0]

        product.product_name = request.POST['product_name']
        product.description = request.POST['description']
        product.brand = shop.name
        size, compound_name, compound_percentage, compound, price, amount = [], [], [], [], [], []
        for i in range(0, 16):
            if request.POST.get(f'size_{i}'):
                size += [request.POST.get(f'size_{i}')]
            if request.POST.get(f'compName_{i}'):
                compound_name += [request.POST.get(f'compName_{i}')]
            if request.POST.get(f'compPercentage_{i}'):
                compound_percentage += [request.POST.get(f'compPercentage_{i}')]
            if request.POST.get(f'price_{i}'):
                price += [request.POST.get(f'price_{i}')]
            if request.POST.get(f'amount_{i}'):
                amount += [request.POST.get(f'amount_{i}')]
        for name, percentage in zip(compound_name, compound_percentage):
            compound += [f"{name} | {percentage}"]
        product.size = str(size)[1:-1]
        product.compound = str(compound)[1:-1]
        product.price = str(price)[1:-1]
        product.amount = str(amount)[1:-1]
        product.show_price = price[0]
        product.country = request.POST['country']
        product.category = request.POST['category']
        product.duration = request.POST['duration']
        product.sex = request.POST['sex']
        account = Account.objects.get(email=request.user)
        product.id_creator = account.email
        product.save()
        return HttpResponseRedirect("/becomeCreator/")
     
    if request.method == 'GET' and "product_cards" in request.GET:
        print("CARDS")
    # delete cards
    if request.method == 'GET' and "delete" in request.GET:
        product = Product_creator.objects.get(id=request.GET['delete'])
        product.delete()
        return HttpResponseRedirect("/becomeCreator/")
    # edit cards
    if request.method == 'GET' and "edit" in request.GET:
        product = Product_creator.objects.get(product_id=request.GET['edit'])
        print(product.product_name)
        return HttpResponseRedirect("/becomeCreator/")
    # change status of card
    if request.method == 'POST' and set(["change_status_to_0", "change_status_to_1", "change_status_to_2", "change_status_to_3"]).intersection(request.POST):
        stat = str(set(["change_status_to_0", "change_status_to_1", "change_status_to_2", "change_status_to_3"]).intersection(request.POST))[2:-2]
        product = Cart.objects.get(id=request.POST[f'{stat}'])
        statuses = {
            '0': 'Заказ в обработке',
            '1': 'Заказ в процессе сборки',
            '2': 'Заказ готов',
            '3': 'Заказ в процессе доставки',
            '4': 'Заказ доставлен',
            '5': 'Заказ отменен',
        }
        product.status = stat[-1]
        product.save()
        return HttpResponseRedirect("/becomeCreator/")
        # card rejection
    if request.method == 'POST' and "decline" in request.POST:
        product = Cart.objects.get(id=request.POST['decline'])
        product.delete()
        return HttpResponseRedirect("/becomeCreator/")
    # create/edit partner
    if request.method == "POST" and "partner" in request.POST:
        try:
            partner = Partner.objects.get(email=request.user)
            partner.inn = request.POST['INN']
            partner.name_small = request.POST['short_name']
            partner.payment_account = request.POST['payment_account']
            partner.reg_form = request.POST['reg_form']
            partner.first_name = request.POST['my_first_name']
            partner.last_name = request.POST['my_last_name']
            partner.email = user.email
            partner.save()
        except:
            partner = Partner()
            partner.inn = request.POST['INN']
            partner.name_small = request.POST['short_name']
            partner.payment_account = request.POST['payment_account']
            partner.reg_form = request.POST['reg_form']
            partner.first_name = request.POST['my_first_name']
            partner.last_name = request.POST['my_last_name']
            partner.email = user.email
            partner.save()

    return render(request, 'becomeCreator.html', content)


def becomeCreatorTemplate_page(request, name):
    try:
        creator = Shop.objects.get(email=request.user.email)
        content['first_name'] = creator.first_name
        content['email'] = creator.email
        content['creator_avatar'] = creator.cover
    except:
        user = Account.objects.get(email=request.user.email)
        content['first_name'] = user.first_name
        content['email'] = user.email
        content['creator_avatar'] = user.userImage
    path = f"becomeCreatorTemplates/template{name}.html"

    if name == '1':
        try:
            partner = Partner.objects.get(email=request.user)
            content['partner'] = partner
        except:
            partner = Partner()
            content['partner'] = partner

    elif name == '2':
        user = Account.objects.get(email=request.user)

        try:
             
            creator = Account.objects.get(email=request.user)
            content['creator'] = creator

        except:

            creator.save()

    elif name == '3':
        shop = Shop.objects.get(email=request.user)
        categorys = shop.category
        content['shop'] = shop
        content['categorys_saver'] = categorys
        
        content['categorys'] = categorys.strip().split(' ') if categorys.strip().split(' ') != [""] else ""

    elif name == '4':
        account = Account.objects.get(email=request.user)
        products = Orders.objects.filter(id_creator=account.email)
        content['products'] = [{
                                'id_creator' : product.id_creator,
                                'id_user_buy' : product.id_user_buy,
                                'price' : product.price,
                                'duration' : product.duration,
                                'compound' : product.compound,
                                'size' : product.size,
                                'amount' : product.amount,
                                'product_name' : product.product_name,
                                'status' : product.status,
                                'message' : product.message,
                                'is_payed' : product.is_payed,
                                'delivery_address' : product.delivery_address,
                                'date_add' : product.date_add,
                                'img' : product.img,
                                'is_incart' : product.is_incart,
                                }
                            for product in products]
        
    elif name == '5':
        account = Account.objects.get(email=request.user)
        products = Product_creator.objects.filter(id_creator=account.email)
        content['products'] = [{'id': product.id,
                                'id_creator': product.id_creator,
                                'product_name': product.product_name,
                                'country': product.country,
                                'brand': product.brand,
                                'rate_sum': product.rate_sum,
                                'vote_sum': product.vote_sum,
                                'category': product.category,
                                'set': product.size,
                                'price': product.show_price,
                                'description': product.description,
                                'availability': product.availability,
                                'picture1': product.picture1,
                                'picture2': product.picture2,
                                'picture3': product.picture3,
                                }
                               for product in products]

    elif name == '6':
        form = ProductCreateForm()
        content['form8'] = form
        content['shop'] = Shop.objects.get(email=request.user.email)
    
    elif name == '7':
        content['shop'] = Shop.objects.get(email=request.user.email)

    return render(request, path, content)


def partners_page(request):
    if request.user.is_authenticated:

            if request.method == "POST":

                mail = BePartner.objects.create()
                mail.brand_name = request.POST['brand_name']
                mail.name = request.POST['name']
                mail.phone = request.POST['phone']
                mail.city = request.POST['city']
                mail.link = request.POST['link']
                mail.email = request.user.email
                mail.save()
                return HttpResponseRedirect('/')



            return render(request, 'showPartner.html')
    else:
        return HttpResponseRedirect('/')


# shop/product sector
def goodsSearch_page(request, product_name):
    products = Product_creator.objects.filter(
        Q(product_name__icontains=product_name) | Q(country__icontains=product_name) | Q(brand__icontains=product_name)
    )
    content['products'] = products
    return render(request, 'goods.html', content)


def goodsSearch_page_category(request, category):
    categories = {
    'Clothing':'Одежда',
    'Shoes':'Обувь',
    'Bags':'Сумки',
    'Interior':'Интерьер',
    'Accessories':'Аксессуары',
    }
    print(category)
    products = Product_creator.objects.filter( Q(category__icontains=categories[category]) )

    content['category'] = categories[category]
    content['products'] = products
    return render(request, 'goods.html', content)

def goods_page(request):
    products = Product_creator.objects.all()
    content['products'] = products
    for element in content['products']:
        element.flooredrating = math.floor(element.rating)
    
    return render(request, 'goods.html', content)


def cardProduct_page(request, product_id):
    flag = "day"
    dt = datetime.now()
    df = DateFormat(dt)
    df.format(get_format('DATE_FORMAT'))
    product = Product_creator.objects.get(id=product_id)
    shop = Shop.objects.get(email=product.id_creator)
    try:
        # add product to cart
        if request.method == "POST" and "addToCartBtn" in request.POST:
            cart_item = Cart()
            cart_item.id_user_buy = Account.objects.get(email=request.user)
            cart_item.id_creator = product.id_creator
            cart_item.brand = product.brand
            cart_item.duration = product.duration
            cart_item.compound = product.compound
            cart_item.size = product.size
            cart_item.product_name = product.product_name
            cart_item.date_add = date.today()
            cart_item.img = product.picture1
            cart_item.amount = request.POST['amount']
            cart_item.size = request.POST['size']
            sizes = product.size.replace("'", '').split(',')
            prices = product.price.replace("'", '').split(',')
            for i in range(len(sizes)):
                if sizes[i].strip() == request.POST['size'].strip():
                    cart_item.price = int(prices[i].strip()) * int(request.POST['amount'])
                    
            cart_item.save()

            return HttpResponseRedirect(f'/goods/{product_id}/')
        # add coment to product
        if request.method == "POST" and "comment_product" in request.POST:
            product = Product_creator.objects.get(id=product_id)
            comment = Comments_product()
            comment.id_creator = product.id_creator
            comment.comentator_email = request.user
            comment.id_product = product.id
            comment.review = request.POST['review']
            comment.rating = request.POST.get('rating', '0')

            product.rate_sum = product.rate_sum + 1
            product.vote_sum = product.vote_sum + int(request.POST.get('rating', '0'))
            product.rating = (product.vote_sum + int(request.POST.get('rating', '0')))/(product.rate_sum + 1)

            comment.save()
            product.save()
            return HttpResponseRedirect(f'/goods/{product_id}/')
        content['product'] = product
        content['product'].show_price = product.price.replace("'", '').split(",")[0]
        content['product'].sizes = product.size.replace("'", '').split(",")
        content['product'].prices = [int(i.strip()) for i in product.price.replace("'", '').split(",")]
        content['product'].compounds = product.compound.replace("'", '').split(",")
        content['product'].rating = float(str(product.rating)[0:4])
        content['product'].flooredrating = math.floor(product.rating)
        content['shop'] = shop

        messages = Comments_product.objects.filter(id_product=product_id)

        id_comment = product.id_creator
        user_product = Account.objects.get(email=id_comment)
        image_user_product = user_product.userImage
        content['image_user_product'] = image_user_product

        for message in messages:
            # передача картинки пользователя, который выложил отзыв
            id_comment = message.comentator_email
            user_comment = Account.objects.get(email=id_comment)
            image_user = user_comment.userImage
            message.image_user = image_user

            # передача даты создания отзыва
            df_message = DateFormat(message.created_data)
            df_message.format(get_format('DATE_FORMAT'))
            if (int(df_message.y()) - int(df.y()) == 0) and (int(df_message.m()) - int(df.m()) == 0):
                message.created_data = int(df.d()) - int(df_message.d())
                message.flag = flag
            elif (int(df_message.y()) - int(df.y()) == 0) and (int(df_message.m()) - int(df.m()) != 0):
                message.flag = "month"
                message.created_data = int(df_message.m()) - int(df.m())
                content['flag'] = flag

            else:
                message.flag = "year"
                message.created_data = int(df_message.y()) - int(df.y())
                content['flag'] = flag

        content['messages'] = messages

        return render(request, 'cardProduct.html', content)
    except Task.DoesNotExist as e:
        raise Http404 from e


# brand sector
def brands_page(request):
    creators = Shop.objects.all()
    persons = Account.objects.all()
    brands = Shop.objects.all()
    content['brands'] = [{
        'name': brand.name,
        'logoImage': brand.logoImage,
        'bgImage': brand.bgImage,
        'description': brand.description,
        'category': brand.category,
        'status': brand.status,
        'email': brand.email,
        'phone': brand.phone,
    }for brand in brands]
    content['creators'] = [{'name': creator.name,
                            'logoImage': creator.logoImage,
                            'bgImage': creator.bgImage,
                            'description': creator.description,
                            'category': creator.category,
                            'status': creator.status,
                            'email': creator.email,
                            'phone': creator.phone,
                            }
                           for creator, person in zip(creators, persons)]
    return render(request, 'brands.html', content)


def sertCardBrend_page(request, shopnmae):
    profile = Shop.objects.get(name=shopnmae)
    content['profile'] = profile
    products = Product_creator.objects.all()
    content['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture1': product.picture1,
                            'picture2': product.picture2,
                            'picture3': product.picture3,
                            'id_creator': product.id_creator,
                            }
                           for product in products]
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)
        content['link'] = (user.id * profile.id) + user.id + profile.id
    return render(request, 'cardBrand.html', content)

# docunment sector
def documents_page(request):
    return render(request, 'documents.html')

def documentTemplates_page(request, name):
    path = f"documentsTemplates/template{name}.html"
    return render(request, path)


# chat sector
def chat_page(request, room_id):
    useremail = request.user
    user = Account.objects.get(email=useremail)
    companion_id = (int(room_id) - int(user.id)) // (int(user.id) + 1)
    companion = Account.objects.get(id=companion_id)
    content['room_id'] = room_id
    content['companion'] = companion
    if not Chat_room.objects.filter(name=room_id).exists():
        new_room = Chat_room.objects.create(name=room_id, user1 = user.id, user2 = companion_id)
        new_room.save()
    return render(request, 'messanger.html', content)


def chat_page_list(request):
    chats = [ chat.name for chat in Chat_room.objects.filter( Q(user1=request.user.id) | Q(user2=request.user.id))]
    components = [ Account.objects.get(id=((int(i) - request.user.id) // request.user.id))  for i in chats ]
    print(components, chats)
    content['chats'] = [ {'chat_room': chat,
                          'first_name': component.first_name,
                          'last_name': component.last_name,
                          'img': component.userImage.url
                          }  for chat, component in zip(chats, components)]
    print(content['chats'])
    return render(request, 'chatRoom.html', content)