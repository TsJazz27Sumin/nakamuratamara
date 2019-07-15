# import area
from apps.student.models.report import Report
import threading

# CRUDのCUDは、ここに集約する。

class ReportRepository:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(ReportRepository, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def insert(self, report_id, auther_user_id, file_name, google_file_id, target_year, comment, login_user_id):
        
        report = Report(
            report_id = report_id,
            auther_user_id = auther_user_id,
            file_name = file_name,
            google_file_id = google_file_id,
            target_year = target_year,
            comment = comment,
            create_user_id = login_user_id,
            update_user_id = login_user_id,
        )

        report.save()
    
    def delete(self, report):
        report.delete()

