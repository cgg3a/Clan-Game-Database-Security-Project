from django.urls import path
from . import views


urlpatterns = [
    path('user', views.sign_in, name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
    path("profile", views.profie, name="profile"),
    path("clan", views.clan, name="clan"),
    path("transactions", views.transactions, name="transactions"),
    path("payment", views.payment, name="payment")
]