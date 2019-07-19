# import area
from django.db import connection
from collections import namedtuple
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
        start = (target_page -1) * offset
        end = start + offset

        return Report.objects.filter(target_year__icontains=target_year, file_name__icontains=file_name).all().order_by('target_year', 'create_timestamp').reverse()[start:end]
    
    def get_one(self, report_id):
        return Report.objects.filter(report_id=report_id).first()
    
    def exist_same_file_name(self, file_name):
        return Report.objects.filter(file_name=file_name).count() > 0
    
    def custom_query(self):

        sql = 'select sr.report_id,' \
              '       sr.target_year,' \
              '       sa.first_name || sa.last_name user_name,' \
              '       sr.file_name,' \
              '       case ' \
              '        when sdc.download_count is null ' \
              '         then 0 ' \
              '        else sdc.download_count' \
              '       end download_count' \
              '  from student_report sr' \
              ' inner join student_applicationuser sa ' \
              '    on sr.auther_user_id = sa.user_id' \
              '  left outer join (select report_id, count(report_id) download_count' \
              '				        from student_downloadinformation sd' \
              '                    group by report_id) sdc ' \
              '	on sr.report_id = sdc.report_id'

        with connection.cursor() as cursor:
            #cursor.execute("SELECT * FROM weather_data WHERE location_id = %s", [str(pk)])
            cursor.execute(sql)
            result_data = self.__namedtuplefetchall(cursor)

        for data in result_data:
            print(data)

    def __namedtuplefetchall(self, cursor):
        #TODO:Baseクラス的な奴にしたい。
        "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]