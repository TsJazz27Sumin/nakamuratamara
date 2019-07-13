from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView

from apps.student.decorators import decorator
from apps.student.queries.masterquery import MasterQuery
from apps.student.queries.reportquery import ReportQuery

@decorator.authenticate_async("index")
def index(request):
    context = {
        'title': 'User Maintenance',
        'message': 'Success!',
    }
    html = render_to_string('student/user_maintenance.html', context)
    return HttpResponse(html)