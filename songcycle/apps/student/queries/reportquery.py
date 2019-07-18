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
        return Report.objects.all().order_by('target_year', 'create_timestamp').reverse()
    
    def count(self, target_year, file_name):
        return Report.objects.filter(target_year__icontains=target_year, file_name__icontains=file_name).count()

    def select(self, target_year, file_name, target_page, offset):

        print(target_page)

        start = (target_page -1) * offset
        end = start + offset

        return Report.objects.filter(target_year__icontains=target_year, file_name__icontains=file_name).all().order_by('target_year', 'create_timestamp').reverse()[start:end]
    
    def get_one(self, report_id):
        return Report.objects.filter(report_id=report_id).first()
    
    def exist_same_file_name(self, file_name):
        return Report.objects.filter(file_name=file_name).count() > 0