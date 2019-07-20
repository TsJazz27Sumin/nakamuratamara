from django.urls import path
from apps.student.views import reportsearchview
from apps.student.views import reportcreateview
from apps.student.views import accesslogview
from apps.student.views import usermaintenanceview
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
    path('home/user-maintenance/', usermaintenanceview.index, name="user_maintenance")
]