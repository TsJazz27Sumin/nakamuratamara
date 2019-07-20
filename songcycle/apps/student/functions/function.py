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


def get_offset(previous, next, target_page, current_page, limit):
    
    offset = 0

    if(previous):
        target_page = current_page - 1
    elif(next):
        target_page = current_page + 1
    
    offset = (target_page - 1) * limit
    
    return offset, target_page
