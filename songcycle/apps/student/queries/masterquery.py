import threading

class MasterQuery:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(MasterQuery, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    # TODO:できればDBのマスタと連動させたい。
    # 定数系

    ## user_status

    def get_active_user_status(self):
        return "01"

    def get_non_active_user_status(self):
        return "02"

    # TODO:できればDBのマスタと連動させたい。
    ## テンポラリーログインURLの有効期間
    def get_temporary_time(self):
        return 120

    ## TODO 開発と本番で切り替えたい。
    ## root_login_url
    def get_root_login_url(self):
        return "http://127.0.0.1:8000/student/login/?onetimepassword="

    ## event_type

    def get_event_type_request_login(self):
        return "request_login"