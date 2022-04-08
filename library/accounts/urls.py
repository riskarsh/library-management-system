from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("signup/", views.signup, name="account_signup"),
    path("signin/", views.signin, name="account_signin"),
    path("signout/", views.signout, name="account_signout"),
]
