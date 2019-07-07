from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from user_agents import parse

from student.forms import RequestLoginForm
from student.services import loginservice
from student.services import accessinformationservice

class requestLoginView(FormView):
    # こんなURLでアクセスされる想定：http://127.0.0.1:8000/student/request-login/
    form_class = RequestLoginForm
    template_name = "student/request_login.html"

    def form_valid(self, form):

        http_accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        user_agent = parse(self.request.META['HTTP_USER_AGENT'])
        remote_addr = self.request.META['REMOTE_ADDR']
        email = self.request.POST["email"]

        if(loginservice.exist_email(email)):
            accessinformationservice.add_success(http_accept_language, user_agent, remote_addr, email)
            loginservice.send_login_url(email)
        else:
            accessinformationservice.add_fault(http_accept_language, user_agent, remote_addr, email)

            # TODO 
            # pandasでcsvにしてメール送信してデイリーでログ監視したい。
        
        # 失敗してもログインURLを送信したことにする。
        return render(self.request, 'student/request_login_success.html', {})
    
    def form_invalid(self, form):
        http_accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        user_agent = parse(self.request.META['HTTP_USER_AGENT'])
        remote_addr = self.request.META['REMOTE_ADDR']
        email = self.request.POST["email"]

        accessinformationservice.add_fault(http_accept_language, user_agent, remote_addr, email)

        # 失敗してもログインURLを送信したことにする。
        return render(self.request, 'student/request_login_success.html', {})
