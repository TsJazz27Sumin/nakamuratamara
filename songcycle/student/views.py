from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):                             
    return render(request, 'student/index.html')

class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "student/login.html"

# TODO ログアウトできてない疑惑
class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "student/logout.html"