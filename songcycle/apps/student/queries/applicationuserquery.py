# import area
from apps.student.models.applicationuser import ApplicationUser
from apps.student.functions import function
from apps.student.queries.masterquery import MasterQuery
import threading

# CRUDのRは、ここに集約する。

class ApplicationUserQuery:

    __singleton = None
    __master_query = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(ApplicationUserQuery, cls).__new__(cls)
            cls.__master_query = MasterQuery()
        cls.__new_lock.release()
        return cls.__singleton

    def is_active_user(self, email):
        return ApplicationUser.objects.filter(email=email, active=self.__master_query.get_active_user_status_sub_code()).count() == 1

    def get_active_user(self, email):
        return ApplicationUser.objects.filter(email=email, active=self.__master_query.get_active_user_status_sub_code()).first()
