# import area
from datetime import datetime, timedelta

from django.utils.crypto import get_random_string

from student.queries import accessinformationquery
from student.functions import function
from student.services import masterservice
from student.repositories.accessinformationrepository import AccessInformationRepository

def add_success(http_accept_language, user_agent, remote_addr, value):
    __add(http_accept_language, user_agent, remote_addr, value, "", "")

def add_fault(http_accept_language, user_agent, remote_addr, value):
    nowtime = datetime.now()
    
    count = accessinformationquery.get_fault_count(remote_addr, nowtime.strftime('%Y-%m-%d'))

    # 同一日内で5回以上間違えている場合は、不正アクセスとみなして記録するのを止める。
    if(count > 5):
        return

    comment = ""
    if(count == 5):
        comment = "不正アクセスの疑いがあります。"

    __add(http_accept_language, user_agent, remote_addr, "", value, comment)

def __add(http_accept_language, user_agent, remote_addr, success_value, fault_value, comment):

    device_type = "unknown"
    if(user_agent.is_mobile):
        device_type = "mobile"
    if(user_agent.is_tablet):
        device_type = "tablet"
    if(user_agent.is_pc):
        device_type = "pc"
    if(user_agent.is_bot):
        device_type = "bot"

    AccessInformationRepository().insert(
        masterservice.get_event_type_request_login(),
        function.get_value(http_accept_language,""),
        function.get_value(user_agent.browser.family,""),
        function.get_value(user_agent.browser.version_string,""),
        function.get_value(user_agent.os.family,""),
        function.get_value(user_agent.os.version_string,""),
        function.get_value(user_agent.device.family,""),
        function.get_value(user_agent.device.brand,""),
        device_type,
        function.get_value(remote_addr,""), 
        success_value,
        fault_value,
        comment
    )
