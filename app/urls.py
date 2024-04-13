from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("signup", views.userRegister, name="signup"),
    path("login", views.userLogin, name="login"),
    path("tokenfee", views.Token_Fee, name="token fee for slots"),
    path("callback", views.order_callback, name="callback for razorpay"),
]