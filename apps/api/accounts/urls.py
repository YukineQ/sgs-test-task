from django.urls import path

from accounts import views

urlpatterns = [
    path('users/login', views.account_login, name='account-login'),
    path('users', views.account_registration, name='account-registration'),
]
