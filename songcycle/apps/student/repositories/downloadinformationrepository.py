# import area
from apps.student.models.downloadinformation import DownloadInformation
import threading

# CRUDのCUDは、ここに集約する。

class DownloadInformationRepository:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(DownloadInformationRepository, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def insert(self, report_id, user_id):
        
        report = DownloadInformation(
            report_id = report_id,
            user_id = user_id,
        )

        report.save()
    
    def delete(self, donwloadinformation):
        donwloadinformation.delete()

