from django.shortcuts import render
from django.views.generic import FormView
from user_agents import parse

from apps.student.forms.reportsummary.loginform import LoginForm
from apps.student.services.accessinformationservice import AccessInformationService
from apps.student.decorators import decorator


class ReportSummaryView(FormView):
    # こんなURLでアクセスされる想定：http://127.0.0.1:8000/student/report-summary-login/
    form_class = LoginForm
    template_name = "student/reportsummary/index.html"

    @decorator.no_authenticate("form_valid")
    def form_valid(self, form):

        access_information_service = AccessInformationService()

        http_accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        user_agent = parse(self.request.META['HTTP_USER_AGENT'])
        remote_addr = self.request.META['REMOTE_ADDR']
        password = self.request.POST["password"]

        access_information_service.add_success(
            http_accept_language, user_agent, remote_addr, password)
        
        return render(self.request, 'student/reportsummary/summary.html', {})

    @decorator.no_authenticate("form_invalid")
    def form_invalid(self, form):

        access_information_service = AccessInformationService()

        http_accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        user_agent = parse(self.request.META['HTTP_USER_AGENT'])
        remote_addr = self.request.META['REMOTE_ADDR']
        password = self.request.POST["password"]

        access_information_service.add_fault(
            http_accept_language, user_agent, remote_addr, password)

        return render(self.request, 'student/reportsummary/index.html', {})
