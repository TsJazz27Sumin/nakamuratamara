# import area
from apps.student.models.applicationuser import ApplicationUser
from apps.student.queries.masterquery import MasterQuery
import threading

# CRUDのRは、ここに集約する。


class ApplicationUserQuery:

    __singleton = None
    __master_query = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(ApplicationUserQuery, cls).__new__(cls)
            cls.__master_query = MasterQuery()
        cls.__new_lock.release()
        return cls.__singleton

    def is_active_user(self, email):
        acitve_code = self.__master_query.get_active_user_status_sub_code()
        return ApplicationUser.objects.filter(
            email=email, active=acitve_code).count() == 1

    def is_exist_user(self, user_id):
        acitve_code = self.__master_query.get_active_user_status_sub_code()
        return ApplicationUser.objects.filter(
            user_id=user_id, active=acitve_code).count() == 1

    def get_active_user(self, email):
        acitve_code = self.__master_query.get_active_user_status_sub_code()
        return ApplicationUser.objects.filter(
            email=email, active=acitve_code).first()

    def get_active_users(self):
        acitve_code = self.__master_query.get_active_user_status_sub_code()
        return ApplicationUser.objects.filter(
            active=acitve_code).all().order_by('user_id')

    def get_users_name(self, user_ids):
        users = ApplicationUser.objects.filter(
            user_id__in=user_ids).all().order_by('user_id')
        user_name_dictionary = {}

        for user in users:
            user_name_dictionary[user.user_id] = user.first_name + \
                " " + user.last_name

        return user_name_dictionary
