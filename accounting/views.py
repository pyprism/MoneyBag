from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .helpers import AccHelper
from .forms import AccountHeadForm as headForm
from random import randint
from time import time

@login_required
def add_ledger_head(request):
    if request.method == "POST":
        add_ledger_head_form = headForm(request.POST)
        if add_ledger_head_form.is_valid():
            form = add_ledger_head_form.save(commit=False)
            form.user = request.user
            form.type = AccHelper.get_head_type(form.parent_head_code,request.user.id)
            form.head_code = int(time())+randint(1,90)
            form.save()
            messages.info(request,'Ledger head added!')
    else:
        add_ledger_head_form =   headForm()

    heads = AccHelper.get_all_group_heads(request.user)
    context = {'form':add_ledger_head_form,'heads':heads}
    return render(request, 'accounting/add-ledger-head.html',context)

@login_required
def voucher_add(request,voucher_type):
    return render(request, 'accounting/voucher-add.html')
