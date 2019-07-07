from django.views.generic import TemplateView
from . import forms
from . import services
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from user_agents import parse

# def エリア

# TODO
# Home画面での切り替えはAjax
# Ajaxでのリクエストの際はログインチェック

def logout(request):
    request.session.flush()
    return redirect('request_login')

def home(request):
    
    if 'authority' in request.session:
        print(request.session['authority'])
    else:
        # 権限が不明な場合は、強制ログアウト
        return redirect('request_login')

    return render(request, 'student/home.html')

def login(request):

    onetime_password = request.GET.get("onetimepassword")
    active_user = services.get_active_user(onetime_password)

    if(active_user is not None):
        services.update_login_information(active_user)

        # TODO
        # OKだったら、セッションにユーザ情報を登録する。
        request.session['authority'] = active_user.authority

        return redirect('home')

    return render(request, 'student/temporary_url_expired.html')

# class エリア

class requestLoginView(FormView):
    # こんなURLでアクセスされる想定：http://127.0.0.1:8000/student/request-login/
    form_class = forms.RequestLoginForm
    template_name = "student/request_login.html"

    def form_valid(self, form):

        http_accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        user_agent = parse(self.request.META['HTTP_USER_AGENT'])
        remote_addr = self.request.META['REMOTE_ADDR']
        email = self.request.POST["email"]

        if(services.exist_email(email)):
            services.add_success_access_information(http_accept_language, user_agent, remote_addr, email)
            services.send_login_url(email)
        else:
            services.add_fault_access_information(http_accept_language, user_agent, remote_addr, email)

            # TODO 
            # pandasでcsvにしてメール送信してデイリーでログ監視したい。
        
        # 失敗してもログインURLを送信したことにする。
        return render(self.request, 'student/request_login_success.html', {})
    
    def form_invalid(self, form):
        http_accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        user_agent = parse(self.request.META['HTTP_USER_AGENT'])
        remote_addr = self.request.META['REMOTE_ADDR']
        email = self.request.POST["email"]

        services.add_fault_access_information(http_accept_language, user_agent, remote_addr, email)

        # 失敗してもログインURLを送信したことにする。
        return render(self.request, 'student/request_login_success.html', {})