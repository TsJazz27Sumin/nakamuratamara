# import area
import threading
from datetime import datetime

from apps.student.queries.masterquery import MasterQuery
from apps.student.repositories.applicationuserrepository import ApplicationUserRepository
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.queries.numberingmasterquery import NumberingMasterQuery


class ApplicationUserService:

    __singleton = None
    __master_query = None
    __application_user_query = None
    __application_user_repository = None
    __numberingmasterquery = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(ApplicationUserService, cls).__new__(cls)
            cls.__master_query = MasterQuery()
            cls.__application_user_query = ApplicationUserQuery()
            cls.__application_user_repository = ApplicationUserRepository()
            cls.__numberingmasterquery = NumberingMasterQuery()
        cls.__new_lock.release()
        return cls.__singleton

    def save_user(
            self,
            user_id,
            email,
            first_name,
            last_name,
            full_name,
            authority,
            status,
            comment,
            login_user_id):

        if(user_id == ''):
            user_id = self.__numberingmasterquery.get_user_id()

            self.__application_user_repository.insert(
                user_id,
                email,
                first_name,
                last_name,
                full_name,
                authority,
                status,
                comment,
                login_user_id)

            return user_id

        else:
            user = self.__application_user_query.get_user(user_id)

            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.full_name = full_name
            user.authority = authority
            user.status = status
            user.comment = comment
            user.update_user_id = login_user_id
            user.update_timestamp = datetime.now()

            self.__application_user_repository.update(user)

            return user_id
