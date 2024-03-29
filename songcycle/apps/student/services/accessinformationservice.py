# import area
import threading
from datetime import datetime
from apps.student.queries.accessinformationquery import AccessInformationQuery
from apps.student.functions import function
from apps.student.queries.masterquery import MasterQuery
from apps.student.repositories.accessinformationrepository import AccessInformationRepository


class AccessInformationService:

    __singleton = None
    __master_query = None
    __access_information_query = None
    __access_information_repository = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(AccessInformationService, cls).__new__(cls)
            cls.__access_information_query = AccessInformationQuery()
            cls.__access_information_repository = AccessInformationRepository()
            cls.__master_query = MasterQuery()
        cls.__new_lock.release()
        return cls.__singleton

    def add_success(
            self,
            http_accept_language,
            user_agent,
            remote_addr,
            value):
        self.__add(
            http_accept_language,
            user_agent,
            remote_addr,
            value,
            "",
            "")

    def add_fault(self, http_accept_language, user_agent, remote_addr, value):
        nowtime = datetime.now()

        count = self.__access_information_query.get_fault_count(
            remote_addr, nowtime.strftime('%Y-%m-%d'))

        # 同一日内で5回以上間違えている場合は、不正アクセスとみなして記録するのを止める。
        if(count > 5):
            return

        comment = ""
        if(count == 5):
            comment = "不正アクセスの疑いがあります。"

        self.__add(
            http_accept_language,
            user_agent,
            remote_addr,
            "",
            value,
            comment)

    def __add(
            self,
            http_accept_language,
            user_agent,
            remote_addr,
            success_value,
            fault_value,
            comment):

        device_type = "unknown"
        if(user_agent.is_mobile):
            device_type = "mobile"
        if(user_agent.is_tablet):
            device_type = "tablet"
        if(user_agent.is_pc):
            device_type = "pc"
        if(user_agent.is_bot):
            device_type = "bot"

        self.__access_information_repository.insert(
            self.__master_query.get_event_type_request_login(),
            function.get_value(http_accept_language, ""),
            function.get_value(user_agent.browser.family, ""),
            function.get_value(user_agent.browser.version_string, ""),
            function.get_value(user_agent.os.family, ""),
            function.get_value(user_agent.os.version_string, ""),
            function.get_value(user_agent.device.family, ""),
            function.get_value(user_agent.device.brand, ""),
            device_type,
            function.get_value(remote_addr, ""),
            success_value,
            fault_value,
            comment
        )
