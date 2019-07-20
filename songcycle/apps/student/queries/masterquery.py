import threading

from apps.student.models.masterdata import MasterData


class MasterQuery:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(MasterQuery, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def get_value(self, target):

        if(len(target) == 5):
           return MasterData.objects.filter(
               code=target[:3], sub_code=target[3:]).first().value

        return None

    def get_active_user_status_sub_code(self):
        return MasterData.objects.filter(
            code="002", value="active").first().sub_code

    def get_temporary_time(self):
        value = MasterData.objects.filter(
            code="003", sub_code="01").first().value
        return int(value)

    # TODO 開発と本番で切り替えたい。
    def get_root_login_url(self):
        return MasterData.objects.filter(
            code="004", sub_code="01").first().value

    # event_type

    def get_event_type_request_login(self):
        return MasterData.objects.filter(
            code="005", sub_code="01").first().value
