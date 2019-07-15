from django.urls import path
from apps.student.views import reportview
from apps.student.views import accesslogview
from apps.student.views import usermaintenanceview
from apps.student.views import homeview
from apps.student.views import requestloginview

urlpatterns = [
    path('request-login/', requestloginview.requestLoginView.as_view(), name="request_login"),
    path('login/',homeview.login, name="login"),
    path('logout/',homeview.logout, name="logout"),
    path('home/',homeview.home, name="home"),
    path('home/report/',reportview.index, name="report"),
    path('home/report-create/',reportview.create, name="report_create"),
    path('home/report-file-upload/',reportview.file_upload, name="file_upload"),
    path('home/report-save/',reportview.save_report, name="report_save"),
    path('home/report-delete/',reportview.delete_report, name="report_delete"),
    path('home/report-download/',reportview.download_report, name="report_download"),
    path('home/access-log/',accesslogview.index, name="access_log"),
    path('home/user-maintenance/',usermaintenanceview.index, name="user_maintenance")
]