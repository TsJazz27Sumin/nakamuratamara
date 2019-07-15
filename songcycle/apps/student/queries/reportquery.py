# import area
from apps.student.models.report import Report
import threading

# CRUDのRは、ここに集約する。

class ReportQuery:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(ReportQuery, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def select_all(self):
        return Report.objects.all().order_by('create_timestamp').reverse()
    
    def get_one(self, report_id):
        return Report.objects.filter(report_id=report_id).first()
    
    def exist_same_file_name(self, file_name):
        return Report.objects.filter(file_name=file_name).count() > 0