from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .helpers import AccHelper, AccConstant
from .forms import AccountHeadForm as headForm
from random import randint
from time import time
from datetime import datetime
from django.http import JsonResponse
from .models import AccountHead, Transaction, TransactionDetails, DashboardMeta
from django.db.models import Q
import json
from num2words import num2words
from dateutil.relativedelta import relativedelta
from decimal import Decimal
from collections import OrderedDict
from .MBCryptr import MBCryptr
from .decorator import unlock_required

@login_required
@unlock_required
def add_ledger_head(request):
    if request.method == "POST":
        add_ledger_head_form = headForm(request.POST)
        if add_ledger_head_form.is_valid():
            en_key = request.session.get('en_key')
            form = add_ledger_head_form.save(commit=False)
            form.user = request.user
            form.name = MBCryptr.encrypt(en_key,form.name)
            form.type = AccHelper.get_head_type(form.parent_head_code,request.user.id)
            form.head_code = int(time())+randint(1,90)
            form.save()
            messages.info(request,'Ledger head added!')
    else:
        add_ledger_head_form =   headForm()

    heads = AccHelper.get_all_group_heads(request)
    context = {'form':add_ledger_head_form,'heads':heads}
    return render(request, 'accounting/add-ledger-head.html',context)

@login_required
@unlock_required
def add_payment_head(request):
    if request.method == "POST":
        add_ledger_head_form = headForm(request.POST)
        if add_ledger_head_form.is_valid():
            en_key = request.session.get('en_key')
            form = add_ledger_head_form.save(commit=False)
            form.user = request.user
            form.name = MBCryptr.encrypt(en_key,form.name)
            form.type = AccHelper.get_head_type(form.parent_head_code,request.user.id)
            form.head_code = int(time())+randint(1,90)
            form.save()
            messages.info(request,'Payment head added!')
    else:
        add_ledger_head_form =   headForm()

    head_types = [AccConstant.ACC_HEAD_CASH,AccConstant.ACC_HEAD_BANK,AccConstant.ACC_HEAD_MOBILE_BANKING]
    heads = AccHelper.get_certain_group_heads(request,head_types)
    tree = AccHelper.get_heads_tree(request,payments_only=True)

    context = {'form':add_ledger_head_form,'heads':heads, 'tree':tree[0]}
    return render(request, 'accounting/add-payment-head.html',context)


@login_required
@unlock_required
def edit_ledger_head(request):
    if request.method == "POST":
        if request.POST.get('acc_head_id',False) and request.POST.get('name',False):
            en_key = request.session.get('en_key')
            head = AccountHead.objects.filter(pk=request.POST.get('acc_head_id')).first()
            head.name = MBCryptr.encrypt(en_key,request.POST.get('name'))
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
@unlock_required
def all_heads(request):
    heads_tree = AccHelper.get_heads_tree(request)
    context = {'tree':heads_tree[0]}
    return render(request, 'accounting/heads.html',context)

@login_required
@unlock_required
def voucher_add(request,voucher_type):
    en_key = request.session.get('en_key')
    if request.method == "POST":
        if AccHelper.validate_voucher(request.POST):
            voucher_id = AccHelper.create_voucher(request,int(voucher_type))
            if voucher_id:
                messages.info(request, 'Voucher has been added.')
                return redirect('voucher.details', voucher_id=voucher_id)
            else:
                messages.error(request, 'DB transaction error!')
                return redirect('voucher.add', voucher_type=voucher_type)
        else:
            messages.error(request, 'Form not valid, fill up again!')
            return redirect('voucher.add', voucher_type=voucher_type)
    else:
        if int(voucher_type) == AccConstant.VOUCHER_RECEIPT:
            service_heads = AccountHead.objects.filter(user=request.user,parent_head_code=AccConstant.ACC_HEAD_SERVICE_REVENUE)
            heads = AccountHead.objects.filter(Q(user=request.user),Q(parent_head_code=AccConstant.ACC_HEAD_DIRECT_INCOMES) | Q(parent_head_code=AccConstant.ACC_HEAD_LOAN),~Q(id=AccConstant.ACC_HEAD_SERVICE_REVENUE))
        elif int(voucher_type) == AccConstant.VOUCHER_PAYMENT:
            service_heads = AccountHead.objects.filter(user=request.user,parent_head_code=AccConstant.ACC_HEAD_SERVICE_EXPENDITURE)
            heads = AccountHead.objects.filter(Q(user=request.user),Q(parent_head_code=AccConstant.ACC_HEAD_DIRECT_EXPENSES) | Q(parent_head_code=AccConstant.ACC_HEAD_LOAN) | Q(parent_head_code=AccConstant.ACC_HEAD_GENERAL_EXPENDITURE),~Q(id=AccConstant.ACC_HEAD_SERVICE_EXPENDITURE),~Q(id=AccConstant.ACC_HEAD_GENERAL_EXPENDITURE))
        else:
            service_heads = []
            heads = []

        plain_heads = []
        for head in heads:
            plain_heads.append(
                {
                    'id': head.id,
                    'name': MBCryptr.decrypt(en_key,head.name)
                }
            )
        plain_service_heads = []
        for head in service_heads:
            plain_service_heads.append(
                {
                    'id': head.id,
                    'name': MBCryptr.decrypt(en_key,head.name)
                }
            )

        paymentHeads = AccountHead.objects.filter(user=request.user,parent_head_code__in=[AccConstant.ACC_HEAD_CASH,AccConstant.ACC_HEAD_BANK,AccConstant.ACC_HEAD_MOBILE_BANKING]).order_by('id')
        pmList = []
        for payHead in paymentHeads:
            head = {
                'id': payHead.id,
                'text': MBCryptr.decrypt(en_key,payHead.name)
            }
            pmList.append(head)

        context = {'voucher_type':voucher_type, 'service_heads':plain_service_heads, 'heads':plain_heads, 'paymentList':json.dumps(pmList)}
        return render(request, 'accounting/voucher-add.html',context)


@login_required
@unlock_required
def voucher_details(request,voucher_id):
    voucher_info = Transaction.objects.filter(id=voucher_id,user=request.user).first()
    if not voucher_info:
        messages.error(request, 'Voucher not found!')
        return redirect('dashboard')

    if voucher_info.voucher_type == AccConstant.VOUCHER_PAYMENT:
        transaction = TransactionDetails.objects.filter(transaction_id=voucher_info.id,position=AccConstant.DEBIT).select_related("account_head").first()
        opsite_transaction = TransactionDetails.objects.filter(transaction_id=voucher_info.id,position=AccConstant.CREDIT).select_related("account_head").first()

    elif voucher_info.voucher_type == AccConstant.VOUCHER_RECEIPT:
        transaction = TransactionDetails.objects.filter(transaction_id=voucher_info.id,position=AccConstant.CREDIT).select_related("account_head").first()
        opsite_transaction = TransactionDetails.objects.filter(transaction_id=voucher_info.id,position=AccConstant.DEBIT).select_related("account_head").first()
    else:
        transaction = TransactionDetails.objects.filter(transaction_id=voucher_info.id,position=AccConstant.CREDIT).select_related("account_head").first()
        opsite_transaction = TransactionDetails.objects.filter(transaction_id=voucher_info.id,position=AccConstant.DEBIT).select_related("account_head").first()
    #decrypt data
    en_key = request.session.get('en_key')
    transaction.amount = Decimal(MBCryptr.decrypt(en_key,transaction.amount))
    transaction.account_head.name = MBCryptr.decrypt(en_key,transaction.account_head.name)
    opsite_transaction.account_head.name = MBCryptr.decrypt(en_key,opsite_transaction.account_head.name)

    context = {"voucher_info":voucher_info, "transaction": transaction, "opsite_transaction": opsite_transaction, "tkinwords": num2words(transaction.amount)}
    return render(request, 'accounting/voucher-details.html', context)

@login_required
@unlock_required
def acc_voucher_add(request,voucher_type):
    en_key = request.session.get('en_key')
    if request.method == "POST":
        if AccHelper.validate_acc_voucher(request.POST):
            amount = MBCryptr.encrypt(en_key,request.POST.get('amount'))
            transId = AccHelper.create_new_transaction(
                request.user.id,
                None,
                request.POST.get('date'),
                voucher_type,
                request.POST.get('description')
            )
            AccHelper.create_transaction_details(
                transId,
                request.POST.get('debit_head'),
                AccConstant.DEBIT,
                amount
            )
            AccHelper.create_transaction_details(
                transId,
                request.POST.get('credit_head'),
                AccConstant.CREDIT,
                amount
            )
            #for dashbaord meta data payable and receivable
            dr_head = request.POST.get('debit_head')
            cr_head = request.POST.get('credit_head')
            dr_head_info = AccountHead.objects.filter(user=request.user,id=dr_head).first()
            if int(dr_head_info.parent_head_code)==AccConstant.ACC_HEAD_PAYABLE:
                dashboard_meta = DashboardMeta.objects.filter(user=request.user, meta_key='total_payable').first()
                dashboard_meta.meta_value = MBCryptr.encrypt(en_key,str(Decimal(MBCryptr.decrypt(en_key,dashboard_meta.meta_value)) - Decimal(request.POST.get('amount'))))
                dashboard_meta.save()
            elif int(dr_head_info.parent_head_code)==AccConstant.ACC_HEAD_RECEIVABLE:
                dashboard_meta = DashboardMeta.objects.filter(user=request.user, meta_key='total_receivable').first()
                dashboard_meta.meta_value = MBCryptr.encrypt(en_key,str(Decimal(MBCryptr.decrypt(en_key,dashboard_meta.meta_value)) + Decimal(request.POST.get('amount'))))
                dashboard_meta.save()

            cr_head_info = AccountHead.objects.filter(user=request.user, id=cr_head).first()
            if int(cr_head_info.parent_head_code) == AccConstant.ACC_HEAD_PAYABLE:
                dashboard_meta = DashboardMeta.objects.filter(user=request.user, meta_key='total_payable').first()
                dashboard_meta.meta_value = MBCryptr.encrypt(en_key,str(Decimal(MBCryptr.decrypt(en_key,dashboard_meta.meta_value)) + Decimal(request.POST.get('amount'))))
                dashboard_meta.save()
            elif int(cr_head_info.parent_head_code) == AccConstant.ACC_HEAD_RECEIVABLE:
                dashboard_meta = DashboardMeta.objects.filter(user=request.user, meta_key='total_receivable').first()
                dashboard_meta.meta_value = MBCryptr.encrypt(en_key,str(Decimal(MBCryptr.decrypt(en_key,dashboard_meta.meta_value)) - Decimal(request.POST.get('amount'))))
                dashboard_meta.save()



            messages.info(request, 'Voucher has been added.')

        else:
            messages.error(request, 'Form not valid, fill up again!')
        return redirect('acc-voucher.add', voucher_type=voucher_type)
    else:
        if int(voucher_type) == AccConstant.VOUCHER_CONTRA:
            raw_dr_heads = AccountHead.objects.filter(user=request.user,parent_head_code__in=[AccConstant.ACC_HEAD_CASH,AccConstant.ACC_HEAD_BANK]).order_by('name').values_list('id','name')
            dr_heads = []
            for head in raw_dr_heads:
                dr_heads.append([
                    head[0],
                    MBCryptr.decrypt(en_key,head[1])
                ])

            cr_heads = dr_heads
        elif int(voucher_type) == AccConstant.VOUCHER_JOURNAL:
            dr_heads = AccHelper.get_all_child_heads(request.user,en_key)
            cr_heads = dr_heads
        else:
            dr_heads = []
            cr_heads = []


        context = {'voucher_type':voucher_type, 'dr_heads':dr_heads, 'cr_heads':cr_heads}
        return render(request, 'accounting/acc-voucher-add.html',context)


@login_required
@unlock_required
def transaction_statement(request):
    en_key = request.session.get('en_key')
    date_from = request.GET.get('date_from',False)
    date_to = request.GET.get('date_to',False)
    if not date_from and not date_to:
        current_date = datetime.today()
        ten_days_before = current_date + relativedelta(days=-10)
        date_from = ten_days_before.strftime('%Y-%m-%d')
        date_to = current_date.strftime('%Y-%m-%d')

    transactions = TransactionDetails.objects.select_related('transaction').filter(
        transaction__user=request.user,
        transaction__transaction_date__range=[date_from,date_to]
    ).select_related('account_head').order_by('-transaction__transaction_date','-position','-transaction__id')

    trans_statements = OrderedDict()
    for transaction in transactions:
        if transaction.position == AccConstant.DEBIT:
            voucher_type = 'Debited'
        else:
            voucher_type = "Credited"

        if transaction.transaction.id in trans_statements:
            account = MBCryptr.decrypt(en_key,transaction.account_head.name) + '(' + voucher_type + ')'
            trans_statements[transaction.transaction.id][0]['accounts'].append(account)
            trans_statements[transaction.transaction.id][0]['description'].append(Decimal(MBCryptr.decrypt(en_key,transaction.amount)))
        else:
            single_trans = {
                'type': AccHelper.get_voucher_type_name(transaction.transaction.voucher_type),
                'date': transaction.transaction.transaction_date,
                'accounts': [MBCryptr.decrypt(en_key,transaction.account_head.name) + '(' + voucher_type + ')'],
                'description': [Decimal(MBCryptr.decrypt(en_key,transaction.amount))]
            }
            trans_statements[transaction.transaction.id] = [single_trans]
    context = {'trans_statements': trans_statements, 'date_from': datetime.strptime(date_from,'%Y-%m-%d'), 'date_to': datetime.strptime(date_to,'%Y-%m-%d')}
    return render(request, 'accounting/report/transaction-statements.html',context)


@login_required
@unlock_required
def income_statement(request):
    month_year = request.GET.get('monthYear', False)
    if not month_year:
        current_date = datetime.today()
        month_year = current_date.strftime('%Y-%m')
    income_statements = AccHelper.generate_income_statement(request,month_year)
    context = {'month_year': datetime.strptime(month_year,'%Y-%m'), 'income_statements': income_statements}
    return render(request, 'accounting/report/income-statements.html',context)


@login_required
@unlock_required
def ledger_statement(request):
    month_year = request.GET.get('monthYear', False)
    head_id = request.GET.get('head_id', False)
    if not month_year:
        current_date = datetime.today()
        month_year = current_date.strftime('%Y-%m')
    if not head_id:
        cash_head = AccountHead.objects.filter(user=request.user, parent_head_code=AccConstant.ACC_HEAD_CASH).first()
        cash_head.name = MBCryptr.decrypt(request.session.get('en_key'),cash_head.name)
        head_id = cash_head.id

    heads = AccHelper.get_heads(request)
    ledger_statements = AccHelper.generate_ledger_statement(request, head_id, month_year)

    context = {'heads':heads, 'head_id':int(head_id), 'month_year': datetime.strptime(month_year,'%Y-%m'), 'ledger_statements': ledger_statements}
    return render(request, 'accounting/report/ledger-statements.html',context)