from django.contrib import messages
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView

from apps.student.decorators import decorator
from apps.student.queries.masterquery import MasterQuery
from apps.student.queries.reportquery import ReportQuery
from apps.student.forms.fileuploadform import FileUploadForm

#TODO:F5対策

@decorator.authenticate_async("index")
def index(request):

    result_list = ReportQuery().select_all()

    context = {
        'title': 'Report',
        'message': 'Success!',
        'result_list':result_list,
        'result_list_count':len(result_list)
    }

    html = render_to_string('student/report/index.html', context)
    return HttpResponse(html)

@decorator.authenticate_admin_only_async("create")
def create(request):
    html = render_to_string('student/report/create.html', request=request)
    return HttpResponse(html)

@decorator.authenticate_admin_only_async_json_response("file_upload")
def file_upload(request):

    form = FileUploadForm(data=request.POST, files=request.FILES)

    json_data = None
    if form.is_valid():
        download_url, file_name = form.save()
        print(download_url)
        print(file_name)
        json_data = {'data':{'message':'Success'}}
    else:
        json_data = {'data':{'message':'Error'}}

    return JsonResponse(json_data)
