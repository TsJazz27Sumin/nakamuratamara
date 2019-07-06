from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView.as_view(), name="login"),
    path('request-login/', views.requestLoginView.as_view(), name="request_login"),
    path('index/',views.index, name="index"),
    path('request-login/success/',views.request_login_success, name="request_login_success")
]