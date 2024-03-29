# import area
from apps.student.models.accessinformation import AccessInformation
import threading

# CRUDのRは、ここに集約する。


class AccessInformationQuery:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(AccessInformationQuery, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def get_fault_count(self, remote_addr, target_date):
        return AccessInformation.objects.filter(
            remote_addr=remote_addr,
            access_date=target_date
        ).exclude(fault_value='').count()

    def select_all(self):
        return AccessInformation.objects.all().order_by(
            'access_date_timestamp').reverse()
