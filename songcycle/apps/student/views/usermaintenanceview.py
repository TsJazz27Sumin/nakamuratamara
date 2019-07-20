from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator


@decorator.authenticate_async("index")
def index(request):
    context = {
        'title': 'User Maintenance',
        'message': 'Success!',
    }
    html = render_to_string('student/usermaintenance/index.html', context)
    return HttpResponse(html)
