from django.conf.urls import url
from accounting import views

urlpatterns = [
    url(r'^add-ledger-head/$', views.add_ledger_head, name='head.add_ledger'),
    url(r'^heads/$', views.all_heads, name='head.all'),
    url(r'^voucher-add/(?P<voucher_type>\d+)/$', views.voucher_add, name='voucher.add'),

]
