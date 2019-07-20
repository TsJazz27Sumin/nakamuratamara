from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.student.decorators import decorator
from apps.student.queries.accessinformationquery import AccessInformationQuery


@decorator.authenticate_async("index")
def index(request):
    #TODO : アクセスログ管理は氏名だけleft outer join

    result_list = AccessInformationQuery().select_all()

    context = {
        'title': 'Access Log',
        'message': 'Success!',
        'result_list': result_list,
        'result_list_count': len(result_list)
    }
    html = render_to_string('student/accesslog/index.html', context)
    return HttpResponse(html)
