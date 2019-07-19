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
from apps.student.queries.downloadinformationquery import DownloadInformationQuery
from apps.student.forms.fileuploadform import FileUploadForm
from apps.student.forms.reportsaveform import ReportSaveForm
from apps.student.forms.reportid import ReportIdForm
from apps.student.forms.reportsearchform import ReportSearchForm
from apps.student.forms.pagingform import PagingForm

__limit = 2

@decorator.authenticate_async("index")
def index(request):

    context = {
        'authority_name': request.session['authority']
    }

    html = render_to_string('student/report/index.html', context, request=request)
    return HttpResponse(html)

@decorator.authenticate_async("search")
def search(request):

    form = ReportSearchForm(data=request.POST)

    result_list = []
    result_list_count = 0
    offset = 0
    if form.is_valid():
        target_year = form.cleaned_data['target_year']
        full_name = form.cleaned_data['full_name']
        file_name = form.cleaned_data['file_name']

        result_list_count = ReportQuery().custom_count(target_year, full_name, file_name)
        result_list = ReportQuery().custom_query(target_year, full_name, file_name, offset, __limit, 'target-year-sort', True)

        request.session['target_year'] = target_year
        request.session['full_name'] = full_name
        request.session['file_name'] = file_name

    context = {
        'result_list':result_list,
        'result_list_count': result_list_count,
        'current_sort_item':'targetYearSort',
        'current_descending_order':True,
        'current_page': offset + 1,
        'limit': __limit,
        'authority_name': request.session['authority']
    }

    html = render_to_string('student/report/search_result.html', context, request=request)
    return HttpResponse(html)

@decorator.authenticate_async("paging")
def paging(request):

    form = PagingForm(data=request.POST)

    if form.is_valid():
        current_page = form.cleaned_data['current_page']
        previous = form.cleaned_data['previous']
        next = form.cleaned_data['next']
        target_page = form.cleaned_data['target_page']

        return __paging(request, current_page, previous, next, target_page)
    else:
        return None

def __paging(request, current_page, previous, next, target_page):
    result_list = []
    result_list_count = 0

    offset = 0

    if(previous):
        target_page = current_page - 1
    elif(next):
        target_page = current_page + 1

    offset = (target_page - 1) * __limit
    
    target_year = request.session['target_year']
    full_name = request.session['full_name']
    file_name = request.session['file_name']

    result_list_count = ReportQuery().custom_count(target_year, full_name, file_name)
    result_list = ReportQuery().custom_query(target_year, full_name, file_name, offset, __limit, 'target-year-sort', True)

    context = {
        'result_list':result_list,
        'result_list_count': result_list_count,
        'current_page': target_page,
        'limit': __limit,
        'authority_name': request.session['authority']
    }

    html = render_to_string('student/report/search_result.html', context, request=request)
    return HttpResponse(html)

@decorator.authenticate_admin_only_async("create")
def create(request):

    context = {
        'choices': __get_choices(),
        'target_years':__get_target_years()
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
        target_year = form.cleaned_data['target_year']
        comment = form.cleaned_data['comment']
        login_user_id = request.session['user_id']

        if(ReportQuery().exist_same_file_name(file_name)):
            json_data = {'data':{'result':'false', 'message':'Already same name file uploaded.'}}
            return JsonResponse(json_data)

        report_id = ReportService().save_report(file_name, file_path, auther_user_id, target_year, comment, login_user_id)

        if(report_id is not None):
            json_data = {'data':{'result':'true', 'message':'Success'}}
            return JsonResponse(json_data)

    else:
        error_message_list = []
        error_item_list = []

        for field in form:
            for error in field.errors:
                # 今んとこ先生が使うので、メッセージは英語のまま。
                if "file_path" in field.name:
                    error_message_list.append("Report File:" + error)
                    error_item_list.append("report-file")
                if "auther_user_id" in field.name:
                    error_message_list.append("Author:" + error)
                    error_item_list.append("auther-user")
                if "target_year" in field.name:
                    error_message_list.append("Year:" + error)
                    error_item_list.append("target-year")
                if "comment" in field.name:
                    error_message_list.append("Comment:" + error)
                    error_item_list.append("comment-area")

        error_message = ','.join(error_message_list)
        error_item = ','.join(error_item_list)
        json_data = {'data':{'result':'false', 'errorMessage':error_message, 'errorItem':error_item}}

    return JsonResponse(json_data)

@decorator.authenticate_admin_only_async("delete_report")
def delete_report(request):

    form = ReportIdForm(data=request.POST)

    if form.is_valid():
        report_id = form.cleaned_data['report_id']
        current_page = form.cleaned_data['current_page']

        ReportService().delete_report(report_id)

        return __paging(request, current_page, False, False, current_page)
    else:
        return None

@decorator.authenticate_admin_only("download_report")
def download_report(request):

    user_id = request.session['user_id']
    report_id = request.GET.get("report_id")

    file, file_name = ReportService().download_report(report_id, user_id)

    response = HttpResponse(file, content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = "filename=" + file_name

    return response

def __get_choices():
    choices = []
    active_users = ApplicationUserQuery().get_active_users()

    for active_user in active_users:
        choices.append((active_user.user_id, active_user.first_name + active_user.last_name))
    
    return choices

def __get_target_years():
    target_years = []

    for i in range(2019, 2039):
        target_years.append((i, i))
    
    return target_years

def __get_ids(result_list):

    user_ids = []
    report_ids = []
    for result in result_list:
        user_ids.append(result.auther_user_id)
        report_ids.append(result.report_id)
    
    user_ids_uniq = list(set(user_ids))

    return user_ids_uniq, report_ids