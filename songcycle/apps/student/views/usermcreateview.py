from django.http import HttpResponse
from django.http.response import JsonResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator


@decorator.authenticate_async("create")
def create(request):

    context = {
        
    }

    html = render_to_string(
        'student/userm/create.html',
        context=context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_async("save_user")
def save_user(request):

    return None
