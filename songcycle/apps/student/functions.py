# import area

# DBアクセスを伴わない関数は、ここに集約する。

def get_value(value, default_value):
    if(value is None):
        return default_value
    return value

# TODO:できればDBのマスタと連動させたい。
# 定数系

def get_active_user_status():
    return "01"

def get_non_active_user_status():
    return "02"

def get_event_type_request_login():
    return "request_login"