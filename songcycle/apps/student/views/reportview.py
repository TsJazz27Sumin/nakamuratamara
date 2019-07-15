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
        'result_list':result_list,
        'result_list_count':len(result_list),
        'authority_name': request.session['authority']
    }

    html = render_to_string('student/report/index.html', context)
    return HttpResponse(html)

@decorator.authenticate_admin_only_async("create")
def create(request):

    context = {
        'choices': __get_choices()
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

@decorator.authenticate_admin_only_async_json_response("save_report")
def save_report(request):

    form = ReportSaveForm(data=request.POST)
    json_data = None

    if form.is_valid():
        file_name = form.cleaned_data['file_name']
        file_path = form.cleaned_data['file_path']
        auther_user_id = form.cleaned_data['auther_user_id']
        comment = form.cleaned_data['comment']
        login_user_id = request.session['user_id']

        report_id = ReportService().save_report(file_name, file_path, auther_user_id, comment, login_user_id)

        if(report_id is not None):
            json_data = {'data':{'result':'true', 'message':'Success'}}
            return JsonResponse(json_data)

    else:
        error_message_list = []

        for field in form:
            for error in field.errors:
                # 今んとこ先生が使うので、メッセージは英語のまま。
                if "file_path" in field.name:
                    error_message_list.append("Report File:" + error)
                if "auther_user_id" in field.name:
                    error_message_list.append("Author:" + error)
                if "comment" in field.name:
                    error_message_list.append("Comment:" + error)

        error_message = '\n'.join(error_message_list)
        json_data = {'data':{'result':'false', 'message':error_message}}

    return JsonResponse(json_data)

@decorator.authenticate_admin_only_async_json_response("delete_report")
def delete_report(request):

    report_id = request.POST['report_id']
    json_data = None

    result = ReportService().delete_report(report_id)

    if(result):
        json_data = {'data':{'message':'Success'}}
        return JsonResponse(json_data)

    return JsonResponse(json_data)

def __get_choices():
    choices = []
    active_users = ApplicationUserQuery().get_active_users()

    for active_user in active_users:
        choices.append((active_user.user_id, active_user.first_name + active_user.last_name))
    
    return choices

