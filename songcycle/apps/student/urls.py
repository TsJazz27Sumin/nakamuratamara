from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginView.as_view(), name="login"),
    path('index/',views.index, name="index")
]