from django.forms import ModelForm
from .models import Transaction, AccountHead, TransactionDetails


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


class AccountHeadForm(ModelForm):
    class Meta:
        model = AccountHead
        fields = '__all__'


class TransactionDetailsForm(ModelForm):
    class Meta:
        model = TransactionDetails
        fields = '__all__'
