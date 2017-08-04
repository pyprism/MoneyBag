from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .helpers import AccHelper, AccConstant
from .forms import AccountHeadForm as headForm
from random import randint
from time import time
from django.http import JsonResponse
from .models import AccountHead


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
    return render(request, 'accounting/add-ledger-head.html',context)\

@login_required
def add_payment_head(request):
    if request.method == "POST":
        add_ledger_head_form = headForm(request.POST)
        if add_ledger_head_form.is_valid():
            form = add_ledger_head_form.save(commit=False)
            form.user = request.user
            form.type = AccHelper.get_head_type(form.parent_head_code,request.user.id)
            form.head_code = int(time())+randint(1,90)
            form.save()
            messages.info(request,'Payment head added!')
    else:
        add_ledger_head_form =   headForm()

    head_types = [AccConstant.ACC_HEAD_CASH,AccConstant.ACC_HEAD_BANK,AccConstant.ACC_HEAD_MOBILE_BANKING]
    heads = AccHelper.get_certain_group_heads(request.user,head_types)
    tree = AccHelper.get_heads_tree(request.user,payments_only=True)

    context = {'form':add_ledger_head_form,'heads':heads, 'tree':tree[0]}
    return render(request, 'accounting/add-payment-head.html',context)\


@login_required
def edit_ledger_head(request):
    if request.method == "POST":
        if request.POST.get('acc_head_id',False) and request.POST.get('name',False):
            head = AccountHead.objects.filter(pk=request.POST.get('acc_head_id')).first()
            head.name = request.POST.get('name')
            head.ledger_head_code = request.POST.get('ledger_head_code')
            head.save()

            return JsonResponse({
                'success': True,
                'message': 'Head Updated!'
            }, safe=False)
        else:
            return JsonResponse({
                'success': False,
                'message': 'Form not valid!'
            }, safe=False)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Method not allowed!'
        }, safe=False)


@login_required
def voucher_add(request,voucher_type):
    return render(request, 'accounting/voucher-add.html')

@login_required
def all_heads(request):
    heads_tree = AccHelper.get_heads_tree(request.user)
    context = {'tree':heads_tree[0]}
    return render(request, 'accounting/heads.html',context)
