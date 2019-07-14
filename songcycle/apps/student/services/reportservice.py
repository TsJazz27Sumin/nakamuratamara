# import area
from datetime import datetime, timedelta
import threading

from apps.student.functions import function
from apps.student.queries.applicationuserquery import ApplicationUserQuery

class ReportService:

    __singleton = None
    __applicationuserrquery = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(ReportService, cls).__new__(cls)
            cls.__applicationuserrquery = ApplicationUserQuery()
        cls.__new_lock.release()
        return cls.__singleton

    def report_save(self, file_name, file_path, auther_user_id, comment):
        
        if(self.__applicationuserrquery.is_active_user(auther_user_id) == False):
            json_data = {'data':{'message':'Error'}}
        #TODO:Google Driveへのアップロード
        #report_idの採番

        return True
