from django.contrib import messages
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from user_agents import parse

from apps.student import forms
from apps.student.decorators import decorator
from apps.student.queries.masterquery import MasterQuery
from apps.student.services.loginservice import LoginService

# def エリア

# TODO
# Home画面での切り替えはAjax

#認証エリア

@decorator.authenticate("home")
def home(request):
    context = {'authority_name': request.session['authority']}

    return render(request, 'student/home.html', context)

@decorator.authenticate("report")
def report(request):
    context = {
        'title': 'Report',
        'message': 'Success!',
    }

    html = render_to_string('student/report.html', context)
    return HttpResponse(html)

@decorator.authenticate("access_log")
def access_log(request):
    #TODO : アクセスログ管理は氏名だけleft outer join
    context = {
        'title': 'Access Log',
        'message': 'Success!',
    }
    html = render_to_string('student/access_log.html', context)
    return HttpResponse(html)

@decorator.authenticate("user_maintenance")
def user_maintenance(request):
    context = {
        'title': 'User Maintenance',
        'message': 'Success!',
    }
    html = render_to_string('student/user_maintenance.html', context)
    return HttpResponse(html)

#非認証エリア

@decorator.no_authenticate("logout")
def logout(request):
    request.session.flush()
    return redirect('request_login')

@decorator.no_authenticate("login")
def login(request):

    login_service = LoginService()

    onetime_password = request.GET.get("onetimepassword")
    active_user = login_service.get_active_user(onetime_password)

    if(active_user is not None):
        login_service.update_login_information(active_user)

        # TODO
        # OKだったら、セッションにユーザ情報を登録する。
        request.session['authority'] = MasterQuery().get_value(active_user.authority)
        request.session['email'] = active_user.email

        return redirect('home')

    return render(request, 'student/temporary_url_expired.html')
