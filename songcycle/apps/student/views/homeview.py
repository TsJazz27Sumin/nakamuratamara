from django.shortcuts import redirect, render

from apps.student.decorators import decorator
from apps.student.queries.masterquery import MasterQuery
from apps.student.services.loginservice import LoginService

#認証エリア


@decorator.authenticate("home")
def home(request):
    context = {'authority_name': request.session['authority']}

    return render(request, 'student/home.html', context)

#非認証エリア


@decorator.no_authenticate("logout")
def logout(request):
    request.session.flush()
    return redirect('request_login')


@decorator.no_authenticate("login")
def login(request):

    login_service = LoginService()

    onetime_password = request.GET.get("onetimepassword")
    active_user = login_service.get_active_user(onetime_password)

    if(active_user is not None):
        login_service.update_login_information(active_user)

        request.session['authority'] = MasterQuery(
        ).get_authority_value(active_user.authority)
        request.session['user_id'] = active_user.user_id

        return redirect('home')

    return render(request, 'student/temporary_url_expired.html')
