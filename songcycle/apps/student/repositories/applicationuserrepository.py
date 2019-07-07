# import area
import threading

# CRUDのCUDは、ここに集約する。

class ApplicationUserRepository:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(ApplicationUserRepository, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def update(self, application_user):
        application_user.save()