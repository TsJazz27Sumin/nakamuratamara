# import area
from apps.student.models.temporarilyloginurl import TemporarilyLoginUrl
import threading

# CRUDのCUDは、ここに集約する。

class TemporarilyLoginUrlRepository:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(TemporarilyLoginUrlRepository, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def insert(self, request_email, onetime_password):
        
        temporarily_login_url = TemporarilyLoginUrl(
            request_email = request_email,
            onetime_password = onetime_password
        )

        temporarily_login_url.save()
