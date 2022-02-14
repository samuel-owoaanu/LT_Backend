from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.enums import Choices
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        if not email:
            raise ValueError(_('Please, enter a valid email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff set to True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be set to true'))
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    GENDER=(
        ('M','Male' ),
        ('F', 'Female')
    )
    email = models.EmailField(_('email_address'), unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    other_names = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=11, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, blank=False)
    date_joined = models.DateTimeField((_('date_joined')), auto_now_add=True)
    is_active = models.BooleanField((_('is_active')), default=True)
    is_staff = models.BooleanField((_('is_staff')), default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'User'
