# import area
from datetime import datetime, timedelta
import threading

from apps.student.functions import function
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.queries.numberingmasterquery import NumberingMasterQuery
from apps.student.services.googleapiservice import GoogleApiService

class ReportService:

    __singleton = None
    __applicationuserrquery = None
    __numberingmasterquery = None
    __googleapiservice = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(ReportService, cls).__new__(cls)
            cls.__applicationuserrquery = ApplicationUserQuery()
            cls.__numberingmasterquery = NumberingMasterQuery()
            cls.__googleapiservice = GoogleApiService()
        cls.__new_lock.release()
        return cls.__singleton

    def report_save(self, file_name, file_path, auther_user_id, comment):
        
        if(self.__applicationuserrquery.is_exist_user(auther_user_id) == False):
            json_data = {'data':{'message':'Error'}}

        # Google Driveへのアップロード
        # https://developers.google.com/drive/api/v3/quickstart/python?hl=ja
        # 初回の認証は必要な様子。

        google_file_id = self.__googleapiservice.upload＿file(file_path, file_name)
        report_id = self.__numberingmasterquery.get_report_id()

        return True
