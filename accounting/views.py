from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def add_ledger_head(request):
    return render(request, 'accounting/add-ledger-head.html')

@login_required
def voucher_add(request,voucher_type):
    return render(request, 'accounting/voucher-add.html')
