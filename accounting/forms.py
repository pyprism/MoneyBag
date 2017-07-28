from django.forms import ModelForm
from .models import Transaction, AccountHead, TransactionDetails


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = ('voucher_status', 'user')


class AccountHeadForm(ModelForm):
    class Meta:
        model = AccountHead
        exclude = ('user','head_code',)


class TransactionDetailsForm(ModelForm):
    class Meta:
        model = TransactionDetails
        fields = '__all__'
