from django.db import models
from django.contrib.auth.models import User


class AccountHead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('AccountHead', on_delete=models.CASCADE)
    name = models.CharField(max_length=400, null=True)
    type = models.CharField(max_length=400, null=True)
    head_code = models.IntegerField(null=True)
    ledger_head_code = models.CharField(max_length=255, null=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)