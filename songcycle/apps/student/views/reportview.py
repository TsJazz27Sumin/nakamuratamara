from django.contrib import messages
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView

from apps.student.decorators import decorator
from apps.student.services.reportservice import ReportService
from apps.student.queries.masterquery import MasterQuery
from apps.student.queries.reportquery import ReportQuery
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.forms.fileuploadform import FileUploadForm
from apps.student.forms.reportsaveform import ReportSaveForm

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

    active_users = ApplicationUserQuery().get_active_users()

    choices = []

    for active_user in active_users:
        choices.append((active_user.user_id, active_user.first_name + active_user.last_name))

    context = {
        'choices': choices,
    }

    html = render_to_string('student/report/create.html', context=context, request=request)
    return HttpResponse(html)

@decorator.authenticate_admin_only_async_json_response("file_upload")
def file_upload(request):

    form = FileUploadForm(data=request.POST, files=request.FILES)

    json_data = None
    if form.is_valid():
        file_path = form.save()
        json_data = {'data':{'message':'Success', 'filePath':file_path}}
    else:
        json_data = {'data':{'message':'Error'}}

    return JsonResponse(json_data)

@decorator.authenticate_admin_only_async_json_response("save")
def report_save(request):

    form = ReportSaveForm(data=request.POST)

    json_data = None
    if form.is_valid():
        file_name = form.cleaned_data['file_name']
        file_path = form.cleaned_data['file_path']
        auther_user_id = form.cleaned_data['auther_user_id']
        comment = form.cleaned_data['comment']

        result = ReportService().report_save(file_name, file_path, auther_user_id, comment)

        if(result):
            json_data = {'data':{'message':'Success'}}
            return JsonResponse(json_data)

    json_data = {'data':{'message':'Error'}}

    return JsonResponse(json_data)
