from django.db import models
from django.contrib.auth.models import User


class AccountHead(models.Model):
    HEAD_TYPES = (
        ("ast", 'asset'),
        ("lib", 'liability'),
        ("oe", 'owners equity'),
        ("exp", 'expense'),
        ("inc", 'income'),
    )
    user = models.ForeignKey(User)
    parent_id = models.ForeignKey('AccountHead', null=True, blank=True)
    name = models.CharField(max_length=400, null=True, blank=True)
    type = models.CharField(choices=HEAD_TYPES, max_length=5, null=True, blank=True)
    head_code = models.IntegerField(null=True)
    ledger_head_code = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounting_account_head'


class Transaction(models.Model):
    STATUS_TYPES = (
        (0, 'disabled'),
        (1, 'entered'),
        (2, 'processing'),
        (3, 'processed'),
    )

    VOUCHER_TYPES = (
        (1, 'Purchase'),
        (5, 'Expense'),
        (3, 'Journal'),
        (4, 'Contra'),
        (5, 'Payment'),
        (6, 'Receipt'),
        (7, 'Debit note'),
        (8, 'Credit note'),
    )

    user = models.ForeignKey(User)
    transaction_date = models.DateTimeField(null=True, blank=True)
    transaction_ref = models.ForeignKey('Transaction', null=True, blank=True)
    voucher_type = models.SmallIntegerField(choices=VOUCHER_TYPES)
    voucher_number = models.CharField(max_length=255, null=True, blank=True)
    voucher_status = models.SmallIntegerField(choices=STATUS_TYPES)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TransactionDetails(models.Model):
    TRANS_POSITION = (
        ("dr", 'debit'),
        ("cr", 'credit'),
    )
    transaction = models.ForeignKey('Transaction')
    account_head = models.ForeignKey('AccountHead')
    position = models.CharField(choices=TRANS_POSITION, max_length=5)
    amount = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        db_table = 'accounting_transaction_details'

