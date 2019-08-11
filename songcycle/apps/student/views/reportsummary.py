from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from user_agents import parse
from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.services.accessinformationservice import AccessInformationService
from apps.student.queries.reportquery import ReportQuery
from apps.student.services.reportservice import ReportService
from apps.student.decorators import decorator
from config.settings.develop import REPORT_SUMMARY_PASSWORD
from apps.student.functions import function
from apps.student.forms.reportsummary.targetyearform import TargetYearForm


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

            context = {
                'target_years': function.get_target_years(),
                'target_year': int(target_year)
            }

            return render(
                request,
                'student/reportsummary/summary.html',
                context=context)

    return redirect(
        reverse('report_summary_index') +
        '?targetyear=' +
        target_year)


# ログインエリアではないが、csrfトークンで都度認証しているような形になっている。
@decorator.no_authenticate_async("change")
def change(request):

    form = TargetYearForm(data=request.POST)

    if form.is_valid():
        target_year = form.cleaned_data['target_year']
        
        result_list = ReportQuery().custom_query(
            str(target_year),
            '',
            '',
            0,
            100,
            'auther-user-sort',
            'True')

        context = {
            'result_list': result_list,
            'result_list_count': len(result_list),
            'target_years': function.get_target_years(),
            'target_year': int(target_year),
            'password': REPORT_SUMMARY_PASSWORD
        }

        return render(
            request,
            'student/reportsummary/summarypartial.html',
            context=context)
    else:
        # プルダウン選択でvalidではない場合は、不正操作として何も返さない。
        return None


# ログインエリアではないが、passwordで都度認証しているような形になっている。
# passwordもreport_idも分かっている場合は、直接URL叩けるがそこまではサポートしない。
# そもそもpasswordが分かってたら、一覧エリアに入れる。
@decorator.no_authenticate_download("download_report")
def download_report(request):

    if(REPORT_SUMMARY_PASSWORD != request.GET.get("password")):
        return None

    report_id = request.GET.get("report_id")

    # ログインユーザなしなので、ユーザIDはU0000で共通とする。
    file, file_name = ReportService().download_report(report_id, 'U0000')

    response = HttpResponse(
        file,
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = "filename=" + file_name

    return response
