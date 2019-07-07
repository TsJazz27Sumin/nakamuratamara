# import area
from datetime import datetime, timedelta

from django.utils.crypto import get_random_string

from student import functions
from student.services import masterservice
from student.repositories.applicationuserrepository import ApplicationUserRepository
from student.repositories.temporarilyloginurlrepository import TemporarilyLoginUrlRepository
from student.queries import applicationuserquery
from student.queries import temporarilyloginurlquery
from student.models.accessinformation import AccessInformation

def update_login_information(active_user):
    active_user.last_login_date_timestamp = datetime.now()
    active_user.login_count += 1
    ApplicationUserRepository().update(active_user)

def exist_email(email):
    return applicationuserquery.is_active_user(email)

def send_login_url(email):

    onetime_password = get_random_string(200)
    login_url = masterservice.get_root_login_url() + onetime_password

    TemporarilyLoginUrlRepository().insert(email, onetime_password)

    # TODO 
    # OKだったら、テンポラリーのログインURLを送信する。
    # テンポラリーのデータは、1日経ったらcronで消したい。

    print(login_url)

def get_active_user(onetime_password):
    valid_time = datetime.now() - timedelta(minutes=masterservice.get_temporary_time())

    if(onetime_password is None):
        return None
    
    temporarily_login_url = temporarilyloginurlquery.is_valid_onetime_password(onetime_password, valid_time)

    if(temporarily_login_url is not None):
        email = temporarily_login_url.request_email
        active_user = applicationuserquery.get_active_user(email)

        return active_user
    
    return None
