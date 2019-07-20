from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator
from apps.student.services.reportservice import ReportService
from apps.student.queries.reportquery import ReportQuery
from apps.student.forms.report.reportid import ReportIdForm
from apps.student.forms.report.reportsearchform import ReportSearchForm
from apps.student.forms.pagingform import PagingForm
from apps.student.forms.report.reportsortform import ReportSortForm
from apps.student.functions import function

#TODO:Paging確認のため、とりあえずこの数字。
__limit = 2


@decorator.authenticate_async("index")
def index(request):

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
            form,
            target_year,
            full_name,
            file_name,
            target_sort_item,
            target_descending_order)
    else:
        return None


@decorator.authenticate_async("sort")
def sort(request):

    form = ReportSortForm(data=request.POST)

    if form.is_valid():
        target_year = request.session['target_year']
        full_name = request.session['full_name']
        file_name = request.session['file_name']
        target_sort_item = form.cleaned_data['target_sort_item']
        target_descending_order = form.cleaned_data['target_descending_order']

        return __search(
            request,
            form,
            target_year,
            full_name,
            file_name,
            target_sort_item,
            target_descending_order)
    else:
        function.print_form_error(form)
        return None


def __search(
        request,
        form,
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
        'current_sort_item': target_sort_item,
        'current_descending_order': target_descending_order,
        'authority_name': request.session['authority']
    }

    html = render_to_string(
        'student/report/search_result.html',
        context,
        request=request)
    return HttpResponse(html)


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
    result_list = []
    result_list_count = 0

    offset = 0

    if(previous):
        target_page = current_page - 1
    elif(next):
        target_page = current_page + 1

    offset = (target_page - 1) * __limit

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


@decorator.authenticate_admin_only("download_report")
def download_report(request):

    user_id = request.session['user_id']
    report_id = request.GET.get("report_id")

    file, file_name = ReportService().download_report(report_id, user_id)

    response = HttpResponse(
        file,
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = "filename=" + file_name

    return response
