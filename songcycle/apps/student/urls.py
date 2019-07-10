from django.urls import path
from apps.student.views import homeview
from apps.student.views import requestloginview

urlpatterns = [
    path('request-login/', requestloginview.requestLoginView.as_view(), name="request_login"),
    path('login/',homeview.login, name="login"),
    path('logout/',homeview.logout, name="logout"),
    path('home/',homeview.home, name="home"),
    path('home/report/',homeview.report, name="report")
]