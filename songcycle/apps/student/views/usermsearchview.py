from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator
from apps.student.queries.applicationuserquery import ApplicationUserQuery

# TODO:Paging確認のため、とりあえずこの数字。
__limit = 2


@decorator.authenticate_async("index")
def index(request):

    html = render_to_string(
        'student/usermaintenance/index.html',
        request=request)

    return HttpResponse(html)


@decorator.authenticate_async("search")
def search(request):

    email = ''
    full_name = ''
    offset = 0
    target_sort_item = 'user-id-sort'
    target_descending_order = 'True'

    result_list_count = ApplicationUserQuery().custom_count(email, full_name)
    result_list = ApplicationUserQuery().custom_query(
        email,
        full_name,
        offset,
        __limit,
        target_sort_item,
        target_descending_order)

    print(result_list_count)
    print(result_list)

    context = {
        'result_list': result_list,
        'result_list_count': result_list_count,
        'current_sort_item': target_sort_item,
        'current_descending_order': target_descending_order,
        'current_page': offset + 1,
        'limit': __limit,
        'current_sort_item': target_sort_item,
        'current_descending_order': target_descending_order,
        'authority_name': request.session['authority']
    }

    html = render_to_string(
        'student/usermaintenance/search_result.html',
        context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_async("paging")
def paging(request):
    return None


@decorator.authenticate_async("sort")
def sort(request):
    return None


@decorator.authenticate_async("detail")
def detail(request):
    return None


@decorator.authenticate_async("delete")
def delete(request):
    return None
