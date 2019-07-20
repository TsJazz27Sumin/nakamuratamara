from django.urls import path
from apps.student.views import reportsearchview
from apps.student.views import reportcreateview
from apps.student.views import accesslogview
from apps.student.views import usermsearchview
from apps.student.views import usermcreateview
from apps.student.views import homeview
from apps.student.views import requestloginview

urlpatterns = [
    path('request-login/', requestloginview.requestLoginView.as_view(), name="request_login"),
    path('login/', homeview.login, name="login"),
    path('logout/', homeview.logout, name="logout"),
    path('home/', homeview.home, name="home"),
    # TODO:urlをrestっぽくしたい。
    path('home/report/', reportsearchview.index, name="report"),
    path('home/report-delete/', reportsearchview.delete_report, name="report_delete"),
    path('home/report-download/', reportsearchview.download_report, name="report_download"),
    path('home/report-search/', reportsearchview.search, name="report_search"),
    path('home/report-paging/', reportsearchview.paging, name="report_paging"),
    path('home/report-sort/', reportsearchview.sort, name="report_sort"),
    path('home/report-create/', reportcreateview.create, name="report_create"),
    path('home/report-file-upload/', reportcreateview.file_upload, name="file_upload"),
    path('home/report-save/', reportcreateview.save_report, name="report_save"),
    path('home/access-log/', accesslogview.index, name="access_log"),
    path('home/user-m/', usermsearchview.index, name="user_m"),
    path('home/user-m-search/', usermsearchview.search, name="user_m_search"),
    path('home/user-m-paging/', usermsearchview.paging, name="user_m_paging"),
    path('home/user-m-sort/', usermsearchview.sort, name="user_m_sort"),
    path('home/user-m-detail/', usermsearchview.detail, name="user_m_detail"),
    path('home/user-m-delete/', usermsearchview.delete, name="user_m_delete"),
    path('home/user-m-create/', usermcreateview.create, name="user_m_create"),
]
