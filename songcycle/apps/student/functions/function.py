# import area

# DBアクセスを伴わない関数は、ここに集約する。


def get_value(value, default_value):
    if(value is None):
        return default_value
    return value
    

def get_offset(previous, next, target_page, current_page, limit):
    
    offset = 0

    if(previous):
        target_page = current_page - 1
    elif(next):
        target_page = current_page + 1
    
    offset = (target_page - 1) * limit
    
    return offset, target_page

    
def get_target_years():
    target_years = []

    for i in range(2019, 2039):
        target_years.append((i, i))

    return target_years
