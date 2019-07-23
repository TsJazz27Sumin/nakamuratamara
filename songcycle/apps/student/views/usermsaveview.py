from django.http import HttpResponse
from django.http.response import JsonResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator
from apps.student.queries.masterquery import MasterQuery
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.services.applicationuserservice import ApplicationUserService
from apps.student.forms.userm.usersaveform import UserSaveForm
from apps.student.forms.userm.useridform import UserIdForm


@decorator.authenticate_admin_only_async("create")
def create(request):

    context = {
        'authority_taples': MasterQuery().get_authority_taples(),
        'user_status_taples': MasterQuery().get_user_status_taples()
    }

    html = render_to_string(
        'student/userm/create.html',
        context=context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_admin_only_async("update")
def update(request):

    form = UserIdForm(data=request.POST)

    if form.is_valid():
        user_id = form.cleaned_data['user_id']

        user = ApplicationUserQuery().get_user(user_id)

        context = {
            'user': user,
            'authority_taples': MasterQuery().get_authority_taples(),
            'user_status_taples': MasterQuery().get_user_status_taples()
        }

        html = render_to_string(
            'student/userm/update.html',
            context=context,
            request=request)
        return HttpResponse(html)
    else:
        return None


@decorator.authenticate_admin_only_async_json_response("save_user")
def save_user(request):

    form = UserSaveForm(data=request.POST)
    json_data = None

    if form.is_valid():
        user_id = form.cleaned_data['user_id']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        full_name = first_name + ' ' + last_name
        authority = form.cleaned_data['authority']
        status = form.cleaned_data['status']
        comment = form.cleaned_data['comment']
        login_user_id = request.session['user_id']

        user = None
        if (user_id != ''):
            user = ApplicationUserQuery().get_user(user_id)

        if(__is_exist_same_email(user, email)):
            json_data = {
                'data': {
                    'result': 'false',
                    'errorMessage': 'Already same email exist.',
                    'errorItem': 'email-area'}}
            return JsonResponse(json_data)

        if(__is_exist_same_full_name(user, full_name)):
            json_data = {
                'data': {
                    'result': 'false',
                    'errorMessage': 'Already same name user exist.',
                    'errorItem': 'fisrt_name'}}
            return JsonResponse(json_data)

        user_id = ApplicationUserService().save_user(
            user_id,
            email,
            first_name,
            last_name,
            full_name,
            authority,
            status,
            comment,
            login_user_id)

        if (user_id is not None):
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


def __is_exist_same_email(user, email):

    if (user is None or user.email != email):
        return ApplicationUserQuery().is_exist_same_email(email)


def __is_exist_same_full_name(user, full_name):

    if (user is None or user.full_name != full_name):
        return ApplicationUserQuery().is_exist_same_email(full_name)


def __get_error_infomations(form):

    error_message_list = []
    error_item_list = []

    for field in form:
        for error in field.errors:
            # 今んとこ先生が使うので、メッセージは英語のまま。
            if "email" in field.name:
                error_message_list.append("Email:" + error)
                error_item_list.append("email-area")
            if "first_name" in field.name:
                error_message_list.append("First Name:" + error)
                error_item_list.append("name-area")
            if "last_name" in field.name:
                error_message_list.append("Last Name:" + error)
                error_item_list.append("name-area")
            if "authority" in field.name:
                error_message_list.append("Authority:" + error)
                error_item_list.append("authority")
            if "status" in field.name:
                error_message_list.append("Status:" + error)
                error_item_list.append("status")
            if "comment" in field.name:
                error_message_list.append("Comment:" + error)
                error_item_list.append("comment-area")

    error_message = ','.join(error_message_list)
    error_item = ','.join(error_item_list)

    return error_message, error_item
