# import area
from . import dataaccessors
from . import queryservices
from . import functions
from student.models.accessinformation import AccessInformation
from student.models.temporarilyloginurl import TemporarilyLoginUrl
from datetime import datetime, timedelta
from django.utils.crypto import get_random_string

def update_login_information(active_user):
    active_user.last_login_date_timestamp = datetime.now()
    active_user.login_count += 1
    dataaccessors.save_application_user(active_user)


def exist_email(email):
    return queryservices.is_active_user(email)

def send_login_url(email):

    onetime_password = get_random_string(200)
    login_url = functions.get_root_login_url() + onetime_password

    temporarily_login_url = TemporarilyLoginUrl(
        request_email = email,
        onetime_password = onetime_password
    )

    dataaccessors.save_temporarily_login_url(temporarily_login_url)

    # TODO 
    # OKだったら、テンポラリーのログインURLを送信する。
    # テンポラリーのデータは、1日経ったらcronで消したい。

    print(login_url)

def get_active_user(onetime_password):
    valid_time = datetime.now() - timedelta(minutes=functions.get_temporary_time())

    if(onetime_password is None):
        return None
    
    temporarily_login_url = queryservices.is_valid_onetime_password(onetime_password, valid_time)

    if(temporarily_login_url is not None):
        email = temporarily_login_url.request_email
        active_user = queryservices.get_active_user(email)

        return active_user
    
    return None

def add_success_access_information(http_accept_language, user_agent, remote_addr, value):
    __add_access_information(http_accept_language, user_agent, remote_addr, value, "", "")

def add_fault_access_information(http_accept_language, user_agent, remote_addr, value):
    nowtime = datetime.now()
    
    count = queryservices.get_fault_count(remote_addr, nowtime.strftime('%Y-%m-%d'))

    # 同一日内で5回以上間違えている場合は、不正アクセスとみなして記録するのを止める。
    if(count > 5):
        return

    comment = ""
    if(count == 5):
        comment = "不正アクセスの疑いがあります。"

    __add_access_information(http_accept_language, user_agent, remote_addr, "", value, comment)

def __add_access_information(http_accept_language, user_agent, remote_addr, success_value, fault_value, comment):

    device_type = "unknown"
    if(user_agent.is_mobile):
        device_type = "mobile"
    if(user_agent.is_tablet):
        device_type = "tablet"
    if(user_agent.is_pc):
        device_type = "pc"
    if(user_agent.is_bot):
        device_type = "bot"

    access_information = AccessInformation(
        event_type = functions.get_event_type_request_login(),
        http_accept_language = functions.get_value(http_accept_language,""),
        browser = functions.get_value(user_agent.browser.family,""),
        browser_version = functions.get_value(user_agent.browser.version_string,""),
        os = functions.get_value(user_agent.os.family,""),
        os_version = functions.get_value(user_agent.os.version_string,""),
        device = functions.get_value(user_agent.device.family,""),
        device_brand = functions.get_value(user_agent.device.brand,""),
        device_type = device_type,
        remote_addr = functions.get_value(remote_addr,""), 
        success_value = success_value,
        fault_value = fault_value,
        comment = comment
    )

    dataaccessors.save_access_information(access_information)