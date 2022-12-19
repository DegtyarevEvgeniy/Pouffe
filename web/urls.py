"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authViews
from app import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # technical links
    path('admin/', views.admin_page, name='admin_page'),
    path('restorePassword/', views.forgot_password_page),

    # enterance links
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_page, name='login'),
    # main page lnk
    path('', views.index_page, name='main_page'),

    # user account links
    path('accounts/', include('django.contrib.auth.urls'), name='account'),
    path('edit/', views.edit_profile, name='edit_profile'),

    # chat links
    path('chats/', views.chat_page_list, name='chat_page_list'),
    path('chat/<room_id>/', views.chat_page, name='chat_page'),

    # document links
    path('documents/', views.documents_page, name='documents_page'),
    path('documents/documentsTemplates/<name>/', views.documentTemplates_page, name='documentTemplates_page'),

    #  brand links
    path('brands/', views.brands_page, name='brands_page'),
    path('brands/<shopnmae>', views.sertCardBrend_page, name='sertCardBrend_page'),


    # partner links
    path('partners/', views.partners_page, name='partners_page'),
    path('becomeCreator/', views.becomeCreator_page, name='becomeCreator_page'),
    path('becomeCreator/becomeCreatorTemplates/<name>/', views.becomeCreatorTemplate_page, name='becomeCreatorTemplate_page'),
    
    # goods links
    path('goods/', views.goods_page, name='goods_page'),
    path('goods/<product_id>/', views.cardProduct_page, name='cardProduct_page'),
    path('goods/category/<category>', views.goodsSearch_page_category, name='goodsSearch_page_category'),
    path('goods/search/<product_name>', views.goodsSearch_page, name='goodsSearch_page'),

    # shop links
    path('orders/', views.orders_page, name='orders_page'),
    path('cart/', views.cart_page, name='cart_page'),

    # path('addTask/', views.addTask_page, name='AddTask'),
    # path('addTask/', views.addTask_page),
    # path('yourTasks/editTask/<task_id>/', views.editTask_page),
    # path('yourTasks/infoTask/', views.infoTask_page),

    # static link
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
# error events
handler400 = views.pageNotAccess
handler403 = views.pageMistakeServ
handler404 = views.pageNotFound
handler500 = views.pageNotRequest

