
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
    return 120

## TODO 開発と本番で切り替えたい。
## root_login_url
def get_root_login_url():
    return "http://127.0.0.1:8000/student/login/?onetimepassword="

## event_type

def get_event_type_request_login():
    return "request_login"