from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView

from apps.student.decorators import decorator
from apps.student.queries.masterquery import MasterQuery
from apps.student.queries.reportquery import ReportQuery

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

    context = {
        'title': 'Report Create',
        'message': 'Success!'
    }

    html = render_to_string('student/report/create.html', context)
    return HttpResponse(html)
