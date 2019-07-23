# import area
import threading

# CRUDのCUDは、ここに集約する。
from apps.student.models.applicationuser import ApplicationUser


class ApplicationUserRepository:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(
                ApplicationUserRepository, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def insert(self,
               user_id,
               email,
               first_name,
               last_name,
               full_name,
               authority,
               status,
               comment,
               login_user_id):

        application_user = ApplicationUser(
            user_id=user_id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            authority=authority,
            status=status,
            comment=comment,
            create_user_id=login_user_id,
            update_user_id=login_user_id
        )

        application_user.save()

    def update(self, application_user):
        application_user.save()

    def delete(self, application_user):
        application_user.delete()
