from apps.student.decorators import decorator


@decorator.authenticate_async("create")
def create(request):

    return None
