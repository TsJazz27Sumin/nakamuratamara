from django.urls import path
from . import views

urlpatterns = [
    path('request-login/', views.requestLoginView.as_view(), name="request_login"),
    path('home/',views.home, name="home")
]