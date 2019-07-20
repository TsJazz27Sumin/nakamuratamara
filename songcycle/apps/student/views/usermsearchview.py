from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator
from apps.student.queries.applicationuserquery import ApplicationUserQuery

# TODO:Paging確認のため、とりあえずこの数字。
__limit = 2


@decorator.authenticate_async("index")
def index(request):

    return search(request)

    # html = render_to_string(
    #     'student/usermaintenance/index.html',
    #     request=request)
    # return HttpResponse(html)


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

    }

    html = render_to_string(
        'student/usermaintenance/index.html',
        context,
        request=request)
    return HttpResponse(html)

@decorator.authenticate_async("create")
def create(request):

    return search(request)
