from django.views.generic import TemplateView
from . import forms
from . import services
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from user_agents import parse

# def エリア

# TODO
# Home画面での切り替えはAjax
# Ajaxでのリクエストの際はログインチェック

def home(request):
    # こんなURLでアクセスされる想定：http://127.0.0.1:8000/student/home/?onetimepassword=abc
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
    # こんなURLでアクセスされる想定：http://127.0.0.1:8000/student/request-login/
    form_class = forms.RequestLoginForm
    template_name = "student/request_login.html"

    def form_valid(self, form):

        http_accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        user_agent = parse(self.request.META['HTTP_USER_AGENT'])
        remote_addr = self.request.META['REMOTE_ADDR']
        email = self.request.POST["email"]

        # TODO 
        # メールアドレスが先生が登録済みのものかエラーチェックを追加する。

        if(services.exist_email("mailaddress")):
            print("is_exist_email is true")
            services.add_success_access_information(http_accept_language, user_agent, remote_addr, email)

            # TODO 
            # OKだったら、テンポラリーのログインURLを送信する。
            # DBにテンポラリーのログインURL情報をどのアドレスに送信したかを登録しておく。
            # もちろん有効期限付きで15分以内とか。
            # テンポラリーのデータは、1日経ったらcronで消したい。
        else:
            print("is_exist_email is false")
            services.add_fault_access_information(http_accept_language, user_agent, remote_addr, email)

            # TODO 
            # pandasでcsvにしてメール送信してデイリーでログ監視したい。
        
        return render(self.request, 'student/request_login_success.html', {})
    
    def form_invalid(self, form):
        http_accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        user_agent = parse(self.request.META['HTTP_USER_AGENT'])
        remote_addr = self.request.META['REMOTE_ADDR']
        email = self.request.POST["email"]

        services.add_fault_access_information(http_accept_language, user_agent, remote_addr, email)

        # 失敗してもログインURLを送信したことにする。
        return render(self.request, 'student/request_login_success.html', {})