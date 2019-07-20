# import area
from django.db import connection

from apps.student.models.applicationuser import ApplicationUser
from apps.student.queries.masterquery import MasterQuery
from apps.student.queries.basequery import BaseQuery
import threading

# CRUDのRは、ここに集約する。


class ApplicationUserQuery(BaseQuery):

    __singleton = None
    __master_query = None
    __new_lock = threading.Lock()
    __sort_item_disctionary = {
        "user-id-sort": 'sa.user_id',
        "email-sort": 'sa.email',
        "user-name-sort": 'sa.full_name',
        "authority-sort": 'sa.authority',
        "active-sort": 'sa.active',
        "first_login_date_timestamp-sort": 'sa.first_login_date_timestamp',
        "last_login_date_timestamp-sort": 'sa.last_login_date_timestamp',
        "login_count-sort": 'sa.login_count',
    }

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

    def custom_count(self, email, full_name):
    
        sql = 'select count(sa.user_id) count' \
              '  from student_applicationuser sa' \
              '	where sa.email like @email' \
              '	  and sa.full_name like @full_name' \

        param_list = [
            {"email": self.to_like_value(email)},
            {"full_name": self.to_like_value(full_name)}
        ]

        result = self.fetchone(sql, param_list)

        return result[0]

    def custom_query(
            self,
            email,
            full_name,
            page,
            limit,
            sort_item,
            descending_order):

        sql = 'select sa.user_id,' \
              '       sa.email,' \
              '       sa.full_name,' \
              '       sa.authority,' \
              '       sa.active,' \
              '       sa.first_login_date_timestamp,' \
              '       sa.last_login_date_timestamp,' \
              '       sa.login_count' \
              '  from student_applicationuser sa' \
              '	where sa.email like @email' \
              '	  and sa.full_name like @full_name' \
              '	order by @sort @desc,' \
              '	         sa.create_timestamp desc' \
              '	  limit @limit offset @offset' \

        param_list = [
            {"email": self.to_like_value(email)},
            {"full_name": self.to_like_value(full_name)},
            {"sort": self.__sort_item_disctionary[sort_item]},
            {"desc": "desc" if self._str_to_bool(descending_order) else "asc"},
            {"limit": str(limit)},
            {"offset": str(page)}
        ]

        return self.fetchall(sql, param_list)
