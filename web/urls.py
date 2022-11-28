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
    path('admin/', views.admin_page),
    path('logout/', views.logout_view),
    path('login/', views.login_page, name='signup'),

    path('restorePassword/', views.forgot_password_page),
    path('addTask/', views.addTask_page, name='AddTask'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index_page),
    path('edit/', views.edit_profile),

    path('chats/', views.chat_page_list),
    path('chat/<room_id>/', views.chat_page),

    # zz
    path('partners/', views.partners_page),
    path('documents/', views.documents_page),
    path('documents/documentsTemplates/<name>/', views.documentTemplates_page),
    path('brands/', views.brands_page),
    path('brands/<shopnmae>', views.sertCardBrend_page),
    path('becomeCreator/', views.becomeCreator_page),
    path('becomeCreator/becomeCreatorTemplates/<name>/', views.becomeCreatorTemplate_page),
    path('addTask/', views.addTask_page),
    path('goods/', views.goods_page),
    path('goods/<product_id>/', views.cardProduct_page),
    path('goods/category/<category>', views.goodsSearch_page_category),
    path('goods/search/<product_name>', views.goodsSearch_page),
    path('yourTasks/editTask/<task_id>/', views.editTask_page),
    path('yourTasks/infoTask/', views.infoTask_page),
    path('orders/', views.orders_page),
    path('cart/', views.cart_page),

    
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
handler400 = views.pageNotAccess
handler403 = views.pageMistakeServ
handler404 = views.pageNotFound
handler500 = views.pageNotRequest

