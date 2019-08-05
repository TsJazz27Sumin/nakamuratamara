from django.urls import path
from apps.student.views import reportsearchview
from apps.student.views import reportcreateview
from apps.student.views import accesslogview
from apps.student.views import usermsearchview
from apps.student.views import usermsaveview
from apps.student.views import homeview
from apps.student.views.requestloginview import RequestLoginView

urlpatterns = [
    path('request-login/', RequestLoginView.as_view(), name="request_login"),
    path('login/', homeview.login, name="login"),
    path('logout/', homeview.logout, name="logout"),
    path('home/', homeview.home, name="home"),
    path('home/report/', reportsearchview.index, name="report"),
    path('home/report/delete/', reportsearchview.delete_report, name="report_delete"),
    path('home/report/download/', reportsearchview.download_report, name="report_download"),
    path('home/report/search/', reportsearchview.search, name="report_search"),
    path('home/report/search-sp/', reportsearchview.search_sp, name="report_search_sp"),
    path('home/report/paging/', reportsearchview.paging, name="report_paging"),
    path('home/report/sort/', reportsearchview.sort, name="report_sort"),
    path('home/report/create/', reportcreateview.create, name="report_create"),
    path('home/report/file-upload/', reportcreateview.file_upload, name="file_upload"),
    path('home/report/save/', reportcreateview.save_report, name="report_save"),
    path('home/userm/', usermsearchview.index, name="user_m"),
    path('home/userm/search/', usermsearchview.search, name="user_m_search"),
    path('home/userm/paging/', usermsearchview.paging, name="user_m_paging"),
    path('home/userm/sort/', usermsearchview.sort, name="user_m_sort"),
    path('home/userm/delete/', usermsearchview.delete_user, name="user_m_delete"),
    path('home/userm/create/', usermsaveview.create, name="user_m_create"),
    path('home/userm/update/', usermsaveview.update, name="user_m_update"),
    path('home/userm/save/', usermsaveview.save_user, name="user_m_save"),
    path('home/accesslog/', accesslogview.index, name="access_log"),
    path('home/accesslog/download', accesslogview.download_access_log, name="access_log_download"),
]
