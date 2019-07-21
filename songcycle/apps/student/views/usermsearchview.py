from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator
from apps.student.forms.userm.usersearchform import UserSearchForm
from apps.student.forms.search.pagingform import PagingForm
from apps.student.forms.search.sortform import SortForm
from apps.student.functions import function
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.queries.masterquery import MasterQuery

# TODO:Paging確認のため、とりあえずこの数字。
__limit = 2


@decorator.authenticate_admin_only_async("index")
def index(request):

    html = render_to_string(
        'student/userm/index.html',
        request=request)

    return HttpResponse(html)


@decorator.authenticate_admin_only_async("search")
def search(request):

    form = UserSearchForm(data=request.POST)

    if form.is_valid():
        email = form.cleaned_data['email']
        full_name = form.cleaned_data['full_name']
        target_sort_item = 'last-login-sort'
        target_descending_order = 'True'

        return __search(
            request,
            email,
            full_name,
            target_sort_item,
            target_descending_order)
    else:
        return None


def __search(
        request,
        email,
        full_name,
        target_sort_item,
        target_descending_order):

    offset = 0

    result_list_count = ApplicationUserQuery().custom_count(email, full_name)
    result_list = ApplicationUserQuery().custom_query(
        email,
        full_name,
        offset,
        __limit,
        target_sort_item,
        target_descending_order)

    authority_dictionary = MasterQuery().get_authority_dictionary()
    user_status_dictionary = MasterQuery().get_user_status_dictionary()

    request.session['email'] = email
    request.session['full_name'] = full_name
    request.session['current_sort_item'] = target_sort_item
    request.session['current_descending_order'] = target_descending_order

    context = {
        'result_list': result_list,
        'result_list_count': result_list_count,
        'authority_dictionary': authority_dictionary,
        'user_status_dictionary': user_status_dictionary,
        'current_sort_item': target_sort_item,
        'current_descending_order': target_descending_order,
        'current_page': offset + 1,
        'limit': __limit
    }

    html = render_to_string(
        'student/userm/search_result.html',
        context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_admin_only_async("paging")
def paging(request):

    form = PagingForm(data=request.POST)

    if form.is_valid():
        current_page = form.cleaned_data['current_page']
        previous = form.cleaned_data['previous']
        next = form.cleaned_data['next']
        target_page = form.cleaned_data['target_page']

        return __paging(request, current_page, previous, next, target_page)
    else:
        return None


def __paging(request, current_page, previous, next, target_page):

    offset, target_page = function.get_offset(previous, next, target_page, current_page, __limit)

    email = request.session['email']
    full_name = request.session['full_name']
    current_sort_item = request.session['current_sort_item']
    current_descending_order = request.session['current_descending_order']

    result_list_count = ApplicationUserQuery().custom_count(email, full_name)
    result_list = ApplicationUserQuery().custom_query(
        email,
        full_name,
        offset,
        __limit,
        current_sort_item,
        current_descending_order)

    authority_dictionary = MasterQuery().get_authority_dictionary()
    user_status_dictionary = MasterQuery().get_user_status_dictionary()

    context = {
        'result_list': result_list,
        'result_list_count': result_list_count,
        'authority_dictionary': authority_dictionary,
        'user_status_dictionary': user_status_dictionary,
        'current_page': target_page,
        'limit': __limit,
        'current_sort_item': current_sort_item,
        'current_descending_order': current_descending_order,
        'authority_name': request.session['authority']
    }

    html = render_to_string(
        'student/userm/search_result.html',
        context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_admin_only_async("sort")
def sort(request):
    form = SortForm(data=request.POST)

    if form.is_valid():
        email = request.session['email']
        full_name = request.session['full_name']
        target_sort_item = form.cleaned_data['target_sort_item']
        target_descending_order = form.cleaned_data['target_descending_order']

        return __search(
            request,
            email,
            full_name,
            target_sort_item,
            target_descending_order)
    else:
        return None


@decorator.authenticate_admin_only_async("detail")
def detail(request):
    return None


@decorator.authenticate_admin_only_async("delete")
def delete(request):
    return None
