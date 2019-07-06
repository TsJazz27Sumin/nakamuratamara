from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

def index(request):                             
    return render(request, 'student/index.html')

def request_login_success(request):                             
    return render(request, 'student/request_login_success.html')

class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "student/login.html"

class requestLoginView(FormView):
    form_class = forms.RequestLoginForm
    template_name = "student/request_login.html"
    success_url = reverse_lazy("request_login_success")

# TODO ログアウトできてない疑惑
class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "student/logout.html"