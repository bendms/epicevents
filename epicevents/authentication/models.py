from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        user = self.model(
            email=self.normalize_email(email=email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email, 
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):

    TYPE_CHOICES = [
        ("MANAGEMENT", "Gestion"),
        ("SALES", "Vente"),
        ("SUPPORT", "Support"),
    ]
    
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.firstname + " " + self.lastname
         
    @property
    def is_staff(self):
        return self.is_admin
    
