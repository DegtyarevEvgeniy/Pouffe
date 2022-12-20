from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers

# create a new user
class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, password= None):
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# user class
class Account(AbstractBaseUser):

    username = models.CharField(max_length=1000, default='', unique=False)
    email = models.EmailField(default='', unique=True)
    first_name = models.CharField(max_length=1000, default='')
    last_name = models.CharField(max_length=1000, default='')
    phone = models.IntegerField(default='1')
    city = models.CharField(max_length=1000, default='')
    # liked_brands = models.CharField(max_length=10000, default='')
    # liked_products = models.CharField(max_length=10000, default='')
    userImage = models.ImageField(default='https://i.ibb.co/s3QmZrw/default.png')
    prevUserImage = models.ImageField(default='')
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    inn = models.IntegerField(default=0)
    name_small = models.CharField(max_length=1000,default='')
    nameFull = models.CharField(max_length=1000,default='')
    payment_account = models.IntegerField(default=0)
    reg_form = models.CharField(max_length=20,default='')
    inn = models.IntegerField(default=0)
    ogrn = models.IntegerField(default=0)
    korr_check = models.IntegerField(default=0)
    kpp = models.IntegerField(default=0)
    index = models.IntegerField(default=0)
    bik = models.IntegerField(default=0)
    checking_account = models.IntegerField(default=0)
    fiz_adress = models.CharField(max_length=1000, default='')
    street = models.CharField(max_length=1000,default='')
    is_partner = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
