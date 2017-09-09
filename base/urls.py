from django.conf.urls import url
from base import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^change-password/', views.change_password, name='change_password'),

]
