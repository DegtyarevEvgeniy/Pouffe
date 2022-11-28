from django.shortcuts import render
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


from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404


def pageNotAccess(request, exception):
    return render(request, 'errorPages/400.html')
    
def pageMistakeServ(request, exception):
    return render(request, 'errorPages/403.html')

def pageNotFound(request, exception):
    return render(request, 'errorPages/404.html')

def pageNotRequest(request):
    return render(request, 'errorPages/500.html')

# def gen_menu(request):
#     if request.user.is_authenticated:
#         user = Account.objects.get(email=request.user.email)

#         return {'user': Account.objects.get(email=request.user.email), }

#     else:
#         return {}

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def goodsSearch_page(request, product_name):
    return render(request, 'goods.html')

def goods_page(request):
    return render(request, 'goods.html')

def goodsSearch_page_category(request):
    return render(request, 'goods.html')

def brands_page(request):
    return render(request, 'brands.html')

def sertCardBrend_page(request, shopnmae):
    return render(request, 'cardBrand.html')

def addTask_page(request):  # sourcery skip: hoist-statement-from-if
    return render(request, 'addTask.html')

def becomeCreator_page(request):  # sourcery skip: low-code-quality
    return render(request, 'becomeCreator.html')

def becomeCreatorTemplate_page(request, name):
    path = f"becomeCreatorTemplates/template{name}.html"
    return render(request, path)

def index_page(request):
    return render(request, 'index.html')

def cardProduct_page(request, product_id):
    return render(request, 'cardProduct.html')

def editTask_page(request, task_id):
    return render(request, 'editTask.html')

def infoTask_page(request):
    return render(request, 'infoTask.html')

def edit_profile(request):
    return render(request, "editProfile.html")

def login_page(request):
    return render(request, 'signin.html')

def forgot_password_page(request):
    return render(request, 'forgotPassword.html')

def documents_page(request):
    return render(request, 'documents.html')

def documentTemplates_page(request, name):
    path = f"documentsTemplates/template{name}.html"
    return render(request, path)

def chat_page(request, room_id):
    return render(request, 'messanger.html')

def chat_page_list(request):
    return render(request, 'chatRoom.html')

def cart_page(request):
    return render(request, 'cart.html')

def orders_page(request):
    return render(request, 'orders.html')

def partners_page(request):
    return render(request, 'showPartner.html')

def admin_page(request):
    return render(request, 'admin.html')