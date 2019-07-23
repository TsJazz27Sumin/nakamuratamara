from django.http import HttpResponse
from django.template.loader import render_to_string
from datetime import datetime
import csv

from apps.student.decorators import decorator
from apps.student.queries.accessinformationquery import AccessInformationQuery


@decorator.authenticate_async("index")
def index(request):

    result_list = AccessInformationQuery().select_all()

    context = {
        'title': 'Access Log',
        'message': 'Success!',
        'result_list': result_list,
        'result_list_count': len(result_list)
    }
    html = render_to_string('student/accesslog/index.html', context)
    return HttpResponse(html)


@decorator.authenticate_download("download_access_log")
def download_access_log(request):

    result_list = AccessInformationQuery().select_all()

    today = datetime.now()
    today = "{0:%Y_%m_%d}".format(datetime.now())
    file_name = 'access_log_' + today + '.csv'

    response = HttpResponse(content_type="text/csv")

    response["Content-Disposition"] = "filename=" + file_name

    writer = csv.writer(response)

    header = ['event_type',
              'http_accept_language',
              'browser',
              'browser_version',
              'os',
              'os_version',
              'device',
              'device_brand',
              'device_type',
              'remote_addr',
              'access_date',
              'access_date_timestamp',
              'success_value',
              'fault_value',
              'comment']

    writer.writerow(header)

    for data in result_list:
        writer.writerow([data.event_type,
                         data.http_accept_language,
                         data.browser,
                         data.browser_version,
                         data.os,
                         data.os_version,
                         data.device,
                         data.device_brand,
                         data.device_type,
                         data.remote_addr,
                         data.access_date,
                         data.access_date_timestamp,
                         data.success_value,
                         data.fault_value,
                         data.comment])

    return response
