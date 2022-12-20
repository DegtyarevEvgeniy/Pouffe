import uuid
from django.db import models
from django.forms import ModelForm
from datetime import datetime

class Shop(models.Model):
    name = models.CharField(max_length=50, default='')
    # country = models.CharField(max_length=50, default='')
    logoImage = models.CharField(max_length=500, default='https://i.ibb.co/z7zmCKn/2022-08-28-10-00-15.png')
    prevLogoImage = models.CharField(max_length=500, default='')
    bgImage = models.CharField(max_length=500, default='https://i.ibb.co/z7zmCKn/2022-08-28-10-00-15.png')
    prevBgImage = models.CharField(max_length=500, default='')
    description = models.CharField(max_length=500, default='')
    category = models.CharField(max_length=500, default='')
    status = models.CharField(max_length=500, default='')
    email = models.CharField(max_length=60, default='example@example.com')
    phone = models.CharField(max_length=20, default='')
    shipping_pony_express = models.CharField(max_length=500, default='')
    shipping_yandex_delivery = models.CharField(max_length=500, default='')
    shipping_dostavista = models.CharField(max_length=500, default='')
    shipping_sdek = models.CharField(max_length=500, default='')

class Product_creator(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    id_creator = models.CharField(max_length=200, default='') #кто создал
    product_name = models.CharField('Название', max_length=500, default='')
    country = models.CharField('Страна', max_length=30, default='')
    brand = models.CharField('Бренд', max_length=30, default='')
    rate_sum = models.IntegerField(default=0)
    vote_sum = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    category = models.CharField('Категория', max_length=50, default='')
    sex = models.CharField('Категория', max_length=50, default='')
    compound = models.CharField('Срок получения товара', max_length=50, default='')
    size = models.CharField(max_length=300, default='')
    duration = models.CharField(max_length=300, default='')
    price = models.CharField(max_length=300, default=0)
    show_price = models.CharField(max_length=300, default=0)
    description = models.CharField('Описание', max_length=1000, default='')
    availability = models.CharField('', max_length=100, default='')
    amount = models.CharField(max_length=100, default='')
    picture1 = models.ImageField(default='https://i.ibb.co/z7zmCKn/2022-08-28-10-00-15.png') 
    picture2 = models.ImageField(default='https://i.ibb.co/z7zmCKn/2022-08-28-10-00-15.png') 
    picture3 = models.ImageField(default='https://i.ibb.co/z7zmCKn/2022-08-28-10-00-15.png') 
    prevPicture = models.ImageField(default='')
   

class Cart(models.Model):
    id_creator = models.CharField(max_length=200, default='') 
    brand = models.CharField(max_length=200, default='') 
    id_user_buy = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=200, default='')
    duration = models.CharField(max_length=200, default='')
    compound = models.CharField('Срок получения товара', max_length=50, default='')
    size = models.CharField(max_length=300, default='')
    amount = models.IntegerField()
    product_name = models.CharField(max_length=500, default='')
    status = models.IntegerField(max_length=200, default='0')
    message = models.CharField(max_length=200, default='')
    payment_method = models.CharField(max_length=500, default='картой онлайн')
    img = models.ImageField(default='https://i.ibb.co/z7zmCKn/2022-08-28-10-00-15.png')

class Orders(models.Model):
    id_creator = models.CharField(max_length=200, default='') 
    brand = models.CharField(max_length=200, default='') 
    id_user_buy = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=200, default='')
    duration = models.CharField(max_length=200, default='')
    compound = models.CharField('Срок получения товара', max_length=50, default='')
    size = models.CharField(max_length=300, default='')
    amount = models.IntegerField()
    product_name = models.CharField(max_length=500, default='')
    status = models.IntegerField(max_length=200, default='0')
    message = models.CharField(max_length=200, default='')
    is_payed = models.BooleanField(default=0)
    delivery_address = models.CharField(max_length=500, default='')
    payment_method = models.CharField(max_length=500, default='картой онлайн')
    order_number = models.BigIntegerField(default='0')
    date_receiving = models.DateField(max_length=50, default='2000-01-01') 
    date_add = models.DateField(max_length=50, default='2000-01-01') 
    img = models.ImageField(default='https://i.ibb.co/z7zmCKn/2022-08-28-10-00-15.png')
    is_incart = models.BooleanField(default=1)


class Comments_partner(models.Model):
    id_creator = models.CharField(max_length=200, default='')
    id_partner = models.CharField(max_length=200, default='')
    review = models.CharField(max_length=200, default='')
    rating = models.IntegerField(default='')


class Comments_product(models.Model):
    id_creator = models.CharField(max_length=200, default='')
    comentator_email = models.CharField(max_length=200, default='')
    id_product = models.CharField(max_length=200, default='')
    review = models.CharField(max_length=2000, default='')
    rating = models.IntegerField(default='0')
    created_data = models.DateTimeField(auto_now_add=True)
class Hashtags(models.Model):
    tag_name = models.CharField(max_length=50, default='')


class Partner(models.Model):
    password = models.CharField(max_length=50, default='')
    last_login = models.CharField(max_length=200, default='')
    username = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default='')
    inn = models.IntegerField(default='0000000000')
    name_small = models.CharField(max_length=200, default='')
    name_full = models.CharField(max_length=200, default='')
    reg_form = models.CharField(max_length=200, default='Самозанятый')
    payment_account = models.CharField(max_length=200, default='')

class Chat_room(models.Model):
    name = models.CharField(max_length=100000)
    user1 = models.IntegerField()
    user2 = models.IntegerField()

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class BePartner(models.Model):
    brand_name = models.CharField(max_length=1000000)
    name = models.CharField(max_length=1000000)
    shipping_ayndex = models.CharField(max_length=1000000)
    city = models.CharField(max_length=1000000)
    link = models.CharField(max_length=1000000)
    email = models.CharField(max_length=1000000)
    phone = models.CharField(max_length=1000000)