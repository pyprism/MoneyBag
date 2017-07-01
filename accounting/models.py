from django.db import models
from django.contrib.auth.models import User


class AccountHead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('AccountHead', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=400, null=True, blank=True)
    type = models.CharField(max_length=400, null=True, blank=True)
    head_code = models.IntegerField(null=True)
    ledger_head_code = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(null=True, blank=True)
    transaction_ref = models.ForeignKey('Transaction', null=True, blank=True)
    voucher_type = models.IntegerField(null=True, blank=True)
    voucher_number = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)