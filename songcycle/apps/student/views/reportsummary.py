from django.shortcuts import render
from django.views.generic import FormView
from user_agents import parse
from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.forms.reportsummary.loginform import LoginForm
from apps.student.services.accessinformationservice import AccessInformationService
from apps.student.decorators import decorator
from config.settings.develop import REPORT_SUMMARY_PASSWORD


# こんなURLでアクセスされる想定：http://127.0.0.1:8000/student/report-summary/?targetyear=2019
@decorator.no_authenticate("index")
def index(request):

    targetyear = request.GET.get(key="targetyear", default="2019")
    
    context = {
        'targetyear': targetyear
    }

    html = render_to_string(
        "student/reportsummary/index.html",
        context,
        request=request)
    return HttpResponse(html)


@decorator.no_authenticate("login")
def login(request):
    access_information_service = AccessInformationService()

    http_accept_language = request.META['HTTP_ACCEPT_LANGUAGE']
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    remote_addr = request.META['REMOTE_ADDR']
    postparam = request.POST

    if 'password' in postparam and 'targetyear' in postparam:
        password = postparam["password"]
        targetyear = postparam["targetyear"]

        print(password)
        print(targetyear)

        # TODO：本番と開発環境の切り替え。
        if(REPORT_SUMMARY_PASSWORD == password):
            access_information_service.add_success(
                http_accept_language, user_agent, remote_addr, password)
            
            return render(request, 'student/reportsummary/summary.html', {})
    
    return render(request, 'student/reportsummary/index.html', {})
