# import area
from datetime import datetime, timedelta
import threading

from django.utils.crypto import get_random_string

from student.queries.masterquery import MasterQuery
from student.repositories.applicationuserrepository import ApplicationUserRepository
from student.repositories.temporarilyloginurlrepository import TemporarilyLoginUrlRepository
from student.queries.applicationuserquery import ApplicationUserQuery
from student.queries.temporarilyloginurlquery import TemporarilyLoginUrlQuery
from student.models.accessinformation import AccessInformation

class LoginService:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(LoginService, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def update_login_information(self, active_user):
        active_user.last_login_date_timestamp = datetime.now()
        active_user.login_count += 1
        ApplicationUserRepository().update(active_user)

    def exist_email(self, email):
        return ApplicationUserQuery().is_active_user(email)

    def send_login_url(self, email):

        onetime_password = get_random_string(200)
        login_url = MasterQuery().get_root_login_url() + onetime_password

        TemporarilyLoginUrlRepository().insert(email, onetime_password)

        # TODO 
        # OKだったら、テンポラリーのログインURLを送信する。
        # テンポラリーのデータは、1日経ったらcronで消したい。

        print(login_url)

    def get_active_user(self, onetime_password):
        valid_time = datetime.now() - timedelta(minutes=MasterQuery().get_temporary_time())

        if(onetime_password is None):
            return None
        
        temporarily_login_url = TemporarilyLoginUrlQuery().is_valid_onetime_password(onetime_password, valid_time)

        if(temporarily_login_url is not None):
            email = temporarily_login_url.request_email
            active_user = ApplicationUserQuery().get_active_user(email)

            return active_user
        
        return None
