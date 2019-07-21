from django.http import HttpResponse
from django.http.response import JsonResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator
from apps.student.queries.masterquery import MasterQuery


@decorator.authenticate_async("create")
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


@decorator.authenticate_async("save_user")
def save_user(request):

    return None
