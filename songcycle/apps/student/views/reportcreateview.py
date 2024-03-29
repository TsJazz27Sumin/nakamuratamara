from django.http import HttpResponse
from django.http.response import JsonResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator
from apps.student.forms.report.fileuploadform import FileUploadForm
from apps.student.forms.report.reportsaveform import ReportSaveForm
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.queries.reportquery import ReportQuery
from apps.student.services.reportservice import ReportService
from apps.student.functions import function


@decorator.authenticate_admin_only_async("create")
def create(request):

    context = {
        'choices': __get_choices(),
        'target_years': function.get_target_years()
    }

    html = render_to_string(
        'student/report/create.html',
        context=context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_admin_only_async_json_response("file_upload")
def file_upload(request):

    form = FileUploadForm(data=request.POST, files=request.FILES)

    json_data = None
    if form.is_valid():
        file_path = form.save()
        json_data = {'data': {'message': 'Success', 'filePath': file_path}}
    else:
        json_data = {'data': {'message': 'Error'}}

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
            json_data = {
                'data': {
                    'result': 'false',
                    'message': 'Already same name file uploaded.'}}
            return JsonResponse(json_data)

        report_id = ReportService().save_report(
            file_name,
            file_path,
            auther_user_id,
            target_year,
            comment,
            login_user_id)

        if(report_id is not None):
            json_data = {'data': {'result': 'true', 'message': 'Success'}}
            return JsonResponse(json_data)

    else:

        error_message, error_item = __get_error_infomations(form)

        json_data = {
            'data': {
                'result': 'false',
                'errorMessage': error_message,
                'errorItem': error_item}}

    return JsonResponse(json_data)


def __get_error_infomations(form):

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

    return error_message, error_item


def __get_choices():
    choices = []
    active_users = ApplicationUserQuery().get_active_users()

    for active_user in active_users:
        choices.append(
            (active_user.user_id,
             active_user.first_name +
             active_user.last_name))

    return choices
