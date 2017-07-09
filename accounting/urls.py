from django.conf.urls import url
from accounting import views

urlpatterns = [
    url(r'^dashboard/', views.dashboard, name='dashboard'),
]
