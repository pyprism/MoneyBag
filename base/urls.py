from django.conf.urls import url
from base import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
]
