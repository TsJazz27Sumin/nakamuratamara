# import area

# DBアクセスを伴わない関数は、ここに集約する。


def get_value(value, default_value):
    if(value is None):
        return default_value
    return value


def print_form_error(form):
    for field in form:
        print(field)
        for error in field.errors:
            print(error)
