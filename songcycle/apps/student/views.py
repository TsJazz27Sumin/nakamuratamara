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
    # こんなURLでアクセスされる想定。
    # http://127.0.0.1:8000/student/home/?onetimepassword=abc
    onetime_password = request.GET.get("onetimepassword")

    # TODO
    # テンポラリーのログインURL情報がDBにあるので照合する。
    if(services.exist_onetime_password(onetime_password)):
        # OKだったら、セッションにユーザ情報を登録する。
        return render(request, 'student/home.html')

    print("exist_onetime_password is false")
    # NGだったら、テンポラリーのログインURLが無効になっていることを伝える。
    return render(request, 'student/temporary_url_expired.html')

# class エリア

class requestLoginView(FormView):
    form_class = forms.RequestLoginForm
    template_name = "student/request_login.html"

    def form_valid(self, form):
        print("form_valid called!")

        # TODO 
        # メールアドレスが先生が登録済みのものかエラーチェックを追加する。

        if(services.exist_email("mailaddress")):
            print("is_exist_email is true")

            # TODO 
            # OKだったら、テンポラリーのログインURLを送信する。
            # DBにテンポラリーのログインURL情報をどのアドレスに送信したかを登録しておく。
            # もちろん有効期限付きで15分以内とか。
            # テンポラリーのデータは、1日経ったらcronで消したい。
        else:
            print("is_exist_email is false")

            # TODO 
            # NGだったら、できればWarning出してログを登録して監視したい。
        
        return render(self.request, 'student/request_login_success.html', {})
    
    def form_invalid(self, form):
        print("form_invalid called!")
        # 失敗してもログインURLを送信したことにする。
        # TODO できればWarning出してログ監視したい。
        return render(self.request, 'student/request_login_success.html', {})