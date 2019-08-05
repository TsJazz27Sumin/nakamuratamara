from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from user_agents import parse
from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.services.accessinformationservice import AccessInformationService
from apps.student.queries.reportquery import ReportQuery
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

    http_accept_language = request.META['HTTP_ACCEPT_LANGUAGE']
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    remote_addr = request.META['REMOTE_ADDR']
    postparam = request.POST

    target_year = postparam.get(key="targetyear", default="2019")

    if 'password' in postparam:
        password = postparam["password"]

        # TODO：本番と開発環境の切り替え。
        if(REPORT_SUMMARY_PASSWORD == password):
            AccessInformationService().add_success(
                http_accept_language, user_agent, remote_addr, password)

            result_list = ReportQuery().custom_query(
                target_year,
                '',
                '',
                0,
                100,
                'auther-user-sort',
                'True')

            context = {
                'result_list': result_list
            }

            # TODO：Webとスマホとデザインを分けると思うので、遷移先も分ける。
            return render(
                request,
                'student/reportsummary/summary.html',
                context=context)

    return redirect(
        reverse('report_summary_index') +
        '?targetyear=' +
        target_year)
