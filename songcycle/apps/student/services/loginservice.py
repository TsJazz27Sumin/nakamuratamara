# import area
from datetime import datetime, timedelta
import threading

from django.utils.crypto import get_random_string

from apps.student.queries.masterquery import MasterQuery
from apps.student.repositories.applicationuserrepository import ApplicationUserRepository
from apps.student.repositories.temporarilyloginurlrepository import TemporarilyLoginUrlRepository
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.queries.temporarilyloginurlquery import TemporarilyLoginUrlQuery
from apps.student.models.accessinformation import AccessInformation
from config.settings import develop
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


class LoginService:

    __singleton = None
    __master_query = None
    __application_user_query = None
    __application_user_repository = None
    __temporarily_login_url_query = None
    __temporarily_login_url_repository = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(LoginService, cls).__new__(cls)
            cls.__master_query = MasterQuery()
            cls.__application_user_query = ApplicationUserQuery()
            cls.__application_user_repository = ApplicationUserRepository()
            cls.__temporarily_login_url_query = TemporarilyLoginUrlQuery()
            cls.__temporarily_login_url_repository = TemporarilyLoginUrlRepository()
        cls.__new_lock.release()
        return cls.__singleton

    def update_login_information(self, active_user):
        active_user.last_login_date_timestamp = datetime.now()
        active_user.login_count += 1
        self.__application_user_repository.update(active_user)

    def exist_email(self, email):
        return self.__application_user_query.is_active_user(email)

    def send_login_url(self, email):

        onetime_password = get_random_string(200)
        login_url = self.__master_query.get_root_login_url() + onetime_password

        self.__temporarily_login_url_repository.insert(email, onetime_password)

        # TODO
        # テンポラリーのデータは、1日経ったらcronで消したい。

        print(login_url)

        # メールが送信できることは確認できたのでコメントアウト
        # message = Mail(
        #     from_email=develop.SENDGRID_FROM,
        #     to_emails=email,
        #     subject='ログインURLのお知らせ',
        #     html_content='一時的に有効なログインURLです。<br>' + login_url
        # )

        # sg = SendGridAPIClient(develop.SENDGRID_APIKEY)
        # response = sg.send(message)

    def get_active_user(self, onetime_password):
        valid_time = datetime.now() - timedelta(minutes=self.__master_query.get_temporary_time())

        if(onetime_password is None):
            return None

        temporarily_login_url = self.__temporarily_login_url_query.is_valid_onetime_password(
            onetime_password, valid_time)

        if(temporarily_login_url is not None):
            email = temporarily_login_url.request_email
            active_user = self.__application_user_query.get_active_user(email)

            return active_user

        return None
