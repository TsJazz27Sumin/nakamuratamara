from django.urls import path
from . import views

urlpatterns = [
    path('request-login/', views.requestLoginView.as_view(), name="request_login"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('home/',views.home, name="home")
]