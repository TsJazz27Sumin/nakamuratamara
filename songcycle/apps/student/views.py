from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from . import services
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

# def エリア

def home(request):                             
    return render(request, 'student/home.html')

# class エリア

class requestLoginView(FormView):
    form_class = forms.RequestLoginForm
    template_name = "student/request_login.html"

    def form_valid(self, form):
        print("form_valid called!")

        # TODO 
        # メールアドレスが先生が登録済みのものかエラーチェックを追加する。

        if(services.is_exist_email("mailaddress")):
            print("is_exist_email is true")
            # OKだったら、テンポラリーのログインURLを送信する。
            # DBにテンポラリーのログインURLをどのアドレスに送信したかを登録しておく。
            # もちろん有効期限付きで15分以内とか。
            # テンポラリーのデータは、1日経ったらcronで消したい。
        else:
            print("is_exist_email is false")
            # NGだったら、できればWarning出してログを登録して監視したい。
        
        return render(self.request, 'student/request_login_success.html', {})
    
    def form_invalid(self, form):
        print("form_invalid called!")
        # 失敗してもログインURLを送信したことにする。
        # TODO できればWarning出してログ監視したい。
        return render(self.request, 'student/request_login_success.html', {})

class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "student/login.html"

# TODO ログアウトできてない疑惑
class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "student/logout.html"