# import area
from django.db import connection
from collections import namedtuple
from apps.student.models.report import Report
from apps.student.queries.basequery import BaseQuery
import threading

# CRUDのRは、ここに集約する。

class ReportQuery(BaseQuery):

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

    def custom_count(self, target_year, full_name, file_name):
    
        sql = 'select count(sr.report_id) count' \
              '  from student_report sr' \
              ' inner join student_applicationuser sa ' \
              '    on sr.auther_user_id = sa.user_id' \
              '	where sr.target_year like @target_year' \
              '	  and sa.full_name like @full_name' \
              '	  and sr.file_name like @file_name' \

        param_disctionary = {
            "target_year" : super().to_like_value(target_year),
            "full_name" : super().to_like_value(full_name),
            "file_name" : super().to_like_value(file_name),
        }

        with connection.cursor() as cursor:
            cursor.execute(super().to_with_param_sql(sql, param_disctionary))
            count = cursor.fetchone()

        return count[0]

    def custom_query(self, target_year, full_name, file_name, page, limit):

        sql = 'select sr.report_id,' \
              '       sr.target_year,' \
              '       sa.full_name,' \
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
              '	on sr.report_id = sdc.report_id' \
              '	where sr.target_year like @target_year' \
              '	  and sa.full_name like @full_name' \
              '	  and sr.file_name like @file_name' \
              '	order by sr.target_year desc,' \
              '	         sr.create_timestamp desc' \
              '	  limit @limit offset @offset' \

        param_disctionary = {
            "target_year" : super().to_like_value(target_year),
            "full_name" : super().to_like_value(full_name),
            "file_name" : super().to_like_value(file_name),
            "limit" : str(limit),
            "offset" : str(page),
        }

        print(super().to_with_param_sql(sql, param_disctionary))

        with connection.cursor() as cursor:
            cursor.execute(super().to_with_param_sql(sql, param_disctionary))
            result_data = super().namedtuplefetchall(cursor)
        
        return result_data
