from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from user_agents import parse

from student import forms
from student.decorators import decorator
from student.queries.masterquery import MasterQuery
from student.services.loginservice import LoginService

# def エリア

# TODO
# Home画面での切り替えはAjax
# Ajaxでのリクエストの際はログインチェック

#認証エリア

@decorator.authenticate
def home(request):
    context = {'authority_name': request.session['authority']}
    print(request.session['authority'])
    return render(request, 'student/home.html', context)

#非認証エリア

def logout(request):
    request.session.flush()
    return redirect('request_login')

def login(request):

    login_service = LoginService()

    onetime_password = request.GET.get("onetimepassword")
    active_user = login_service.get_active_user(onetime_password)

    if(active_user is not None):
        login_service.update_login_information(active_user)

        # TODO
        # OKだったら、セッションにユーザ情報を登録する。
        request.session['authority'] = MasterQuery().get_value(active_user.authority)

        return redirect('home')

    return render(request, 'student/temporary_url_expired.html')
