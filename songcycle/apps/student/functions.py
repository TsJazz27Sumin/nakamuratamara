# import area

# DBアクセスを伴わない関数は、ここに集約する。

def get_value(value, default_value):
    if(value is None):
        return default_value
    return value