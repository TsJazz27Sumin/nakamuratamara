import threading
from django.db.models import Count
from apps.student.models.downloadinformation import DownloadInformation


class DownloadInformationQuery:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(DownloadInformationQuery, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def select_all_by_report_id(self, report_id):
        return DownloadInformation.objects.filter(report_id=report_id).all()

    def get_count_dictionary(self, report_ids):
        result_list = DownloadInformation.objects.values('report_id').filter(
            report_id__in=report_ids).order_by('report_id').annotate(
            count=Count('report_id'))

        count_dictionary = {}

        for result in result_list:
            count_dictionary[result['report_id']] = str(result['count'])

        return count_dictionary
