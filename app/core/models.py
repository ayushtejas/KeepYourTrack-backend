from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.conf import settings
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_field):
        if not email:
            raise ValueError('Email can not be empty')
        user = self.model(email= self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,password)
        user.is_superuser = True
        user.save(using = self._db)

class User(AbstractBaseUser, PermissionsMixin):
    '''Users in the system'''

    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    email = models.EmailField(max_length=255, unique= True,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'