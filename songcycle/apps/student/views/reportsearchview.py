from django.http import HttpResponse
from django.template.loader import render_to_string
from user_agents import parse

from apps.student.decorators import decorator
from apps.student.services.reportservice import ReportService
from apps.student.queries.reportquery import ReportQuery
from apps.student.forms.report.reportid import ReportIdForm
from apps.student.forms.report.reportsearchform import ReportSearchForm
from apps.student.forms.report.reportsearchspform import ReportSearchSpForm
from apps.student.forms.search.pagingform import PagingForm
from apps.student.forms.search.sortform import SortForm
from apps.student.functions import function

# TODO:Paging確認のため、とりあえずこの数字。
__limit = 2


@decorator.authenticate_async("index")
def index(request):

    user_agent = parse(request.META['HTTP_USER_AGENT'])

    if(user_agent.is_mobile):
        html = render_to_string(
            'student/report/index_sp.html',
            {},
            request=request)
        return HttpResponse(html)

    context = {
        'authority_name': request.session['authority']
    }

    html = render_to_string(
        'student/report/index.html',
        context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_async("search")
def search(request):

    form = ReportSearchForm(data=request.POST)

    if form.is_valid():
        target_year = form.cleaned_data['target_year']
        full_name = form.cleaned_data['full_name']
        file_name = form.cleaned_data['file_name']
        target_sort_item = 'target-year-sort'
        target_descending_order = 'True'

        return __search(
            request,
            target_year,
            full_name,
            file_name,
            target_sort_item,
            target_descending_order)
    else:
        return None


@decorator.authenticate_async("sort")
def sort(request):

    form = SortForm(data=request.POST)

    if form.is_valid():
        target_year = request.session['target_year']
        full_name = request.session['full_name']
        file_name = request.session['file_name']
        target_sort_item = form.cleaned_data['target_sort_item']
        target_descending_order = form.cleaned_data['target_descending_order']

        return __search(
            request,
            target_year,
            full_name,
            file_name,
            target_sort_item,
            target_descending_order)
    else:
        return None


def __search(
        request,
        target_year,
        full_name,
        file_name,
        target_sort_item,
        target_descending_order):

    offset = 0

    result_list_count = ReportQuery().custom_count(target_year, full_name, file_name)
    result_list = ReportQuery().custom_query(
        target_year,
        full_name,
        file_name,
        offset,
        __limit,
        target_sort_item,
        target_descending_order)

    request.session['target_year'] = target_year
    request.session['full_name'] = full_name
    request.session['file_name'] = file_name
    request.session['current_sort_item'] = target_sort_item
    request.session['current_descending_order'] = target_descending_order

    context = {
        'result_list': result_list,
        'result_list_count': result_list_count,
        'current_sort_item': target_sort_item,
        'current_descending_order': target_descending_order,
        'current_page': offset + 1,
        'limit': __limit,
        'authority_name': request.session['authority']
    }

    html = render_to_string(
        'student/report/search_result.html',
        context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_async("search_sp")
def search_sp(request):

    form = ReportSearchSpForm(data=request.POST)

    if form.is_valid():
        search_value = form.cleaned_data['search_value']

        result_list = ReportQuery().custom_query_sp(search_value)

        context = {
            'result_list': result_list
        }

        html = render_to_string(
            'student/report/search_result_sp.html',
            context,
            request=request)
        return HttpResponse(html)
    else:
        return None


@decorator.authenticate_async("paging")
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

    target_year = request.session['target_year']
    full_name = request.session['full_name']
    file_name = request.session['file_name']
    current_sort_item = request.session['current_sort_item']
    current_descending_order = request.session['current_descending_order']

    result_list_count = ReportQuery().custom_count(target_year, full_name, file_name)
    result_list = ReportQuery().custom_query(
        target_year,
        full_name,
        file_name,
        offset,
        __limit,
        current_sort_item,
        current_descending_order)

    context = {
        'result_list': result_list,
        'result_list_count': result_list_count,
        'current_page': target_page,
        'limit': __limit,
        'current_sort_item': current_sort_item,
        'current_descending_order': current_descending_order,
        'authority_name': request.session['authority']
    }

    html = render_to_string(
        'student/report/search_result.html',
        context,
        request=request)
    return HttpResponse(html)


@decorator.authenticate_admin_only_async("delete_report")
def delete_report(request):

    form = ReportIdForm(data=request.POST)

    if form.is_valid():
        report_id = form.cleaned_data['report_id']
        current_page = form.cleaned_data['current_page']

        ReportService().delete_report(report_id)

        return __paging(request, current_page, False, False, current_page)
    else:
        return None


@decorator.authenticate_async("download_report")
def download_report(request):

    user_id = request.session['user_id']
    report_id = request.GET.get("report_id")

    file, file_name = ReportService().download_report(report_id, user_id)

    response = HttpResponse(
        file,
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = "filename=" + file_name

    return response
