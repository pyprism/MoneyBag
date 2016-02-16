from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class AccountManager(BaseUserManager):

    def create_user(self, username=None, password=None, **kwargs):
        account = self.model(username=username)

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, username, password, **kwargs):
        account = self.create_user(username, password, **kwargs)
        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    objects = AccountManager()


class Budget(models.Model):
    month = models.DateField()
    target = models.DecimalField(max_digits=10, decimal_places=5)
    current = models.DecimalField(max_digits=10, decimal_places=5)


class Balance(models.Model):
    month = models.DateTimeField(auto_now_add=True)
    income = models.DecimalField(max_digits=10, decimal_places=5)
    expense = models.DecimalField(max_digits=10, decimal_places=5)
