# import area
from apps.student.models.accessinformation import AccessInformation
import threading

# CRUDのCUDは、ここに集約する。

class AccessInformationRepository:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(AccessInformationRepository, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def insert(self, event_type, http_accept_language, browser, browser_version, os, os_version, device, device_brand, device_type, 
    remote_addr, success_value, fault_value, comment):
        
        access_information = AccessInformation(
            event_type = event_type,
            http_accept_language = http_accept_language,
            browser = browser,
            browser_version = browser_version,
            os = os,
            os_version = os_version,
            device = device,
            device_brand = device_brand,
            device_type = device_type,
            remote_addr = remote_addr, 
            success_value = success_value,
            fault_value = fault_value,
            comment = comment
        )

        access_information.save()
