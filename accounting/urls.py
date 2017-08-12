from django.conf.urls import url
from accounting import views

urlpatterns = [
    url(r'^add-ledger-head/$', views.add_ledger_head, name='head.add_ledger'),
    url(r'^add-payment-head/$', views.add_payment_head, name='head.add_payment'),
    url(r'^edit-ledger-head/$', views.edit_ledger_head, name='head.edit_ledger'),
    url(r'^heads/$', views.all_heads, name='head.all'),
    url(r'^voucher-add/(?P<voucher_type>\d+)/$', views.voucher_add, name='voucher.add'),
    url(r'^acc-voucher-add/(?P<voucher_type>\d+)/$', views.acc_voucher_add, name='acc-voucher.add'),
    url(r'^voucher-details/(?P<voucher_id>\d+)/$', views.voucher_details, name='voucher.details'),

]
