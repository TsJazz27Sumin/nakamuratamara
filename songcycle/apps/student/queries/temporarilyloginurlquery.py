# import area
from student.models.temporarilyloginurl import TemporarilyLoginUrl
import threading

# CRUDのRは、ここに集約する。

class TemporarilyLoginUrlQuery:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(TemporarilyLoginUrlQuery, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def is_valid_onetime_password(self, onetime_password, valid_timestamp):
        return TemporarilyLoginUrl.objects.filter(onetime_password=onetime_password, send_email_date_timestamp__gt=valid_timestamp).first()