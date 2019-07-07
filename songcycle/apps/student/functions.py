# import area

# DBアクセスを伴わない関数は、ここに集約する。

def get_value(value, default_value):
    if(value is None):
        return default_value
    return value

# TODO:できればDBのマスタと連動させたい。
# 定数系

## user_status

def get_active_user_status():
    return "01"

def get_non_active_user_status():
    return "02"

# TODO:できればDBのマスタと連動させたい。
## テンポラリーログインURLの有効期間
def get_temporary_time():
    return 15

## TODO 開発と本番で切り替えたい。
## root_login_url
def get_root_login_url():
    return "http://127.0.0.1:8000/student/home/?onetimepassword="

## event_type

def get_event_type_request_login():
    return "request_login"