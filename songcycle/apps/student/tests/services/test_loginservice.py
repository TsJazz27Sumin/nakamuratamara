from django.test import TestCase
from django.utils.crypto import get_random_string

from apps.student.repositories.applicationuserrepository import ApplicationUserRepository
from apps.student.repositories.temporarilyloginurlrepository import TemporarilyLoginUrlRepository
from apps.student.services.loginservice import LoginService
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.models.masterdata import MasterData


class LoginServiceTestCase(TestCase):

    def test_update_login_information(self):

        user_id = "U0002"
        email = "email@example.com"
        first_name = "first_name"
        last_name = "last_name"
        full_name = "full_name"
        authority = "01"
        status = "02"
        comment = "comment"
        login_user_id = "U0001"

        ApplicationUserRepository().insert(
            user_id,
            email,
            first_name,
            last_name,
            full_name,
            authority,
            status,
            comment,
            login_user_id)

        user = ApplicationUserQuery().get_user(user_id)

        LoginService().update_login_information(user)

        user = ApplicationUserQuery().get_user(user_id)
        self.assertEqual(user.login_count, 1)

    def test_exist_email(self):

        MasterData.objects.create(
            code="002",
            sub_code="01",
            value='active',
            sub_value='sub_value',
            comment='')

        ApplicationUserRepository().insert(
            "U0002",
            "email2@example.com",
            "first_name2",
            "last_name2",
            "full_name2",
            "01",
            "01",
            "comment2",
            "U0001")

        ApplicationUserRepository().insert(
            "U0003",
            "email3@example.com",
            "first_name3",
            "last_name3",
            "full_name3",
            "02",
            "02",
            "comment3",
            "U0001")

        result = LoginService().exist_email("email2@example.com")

        self.assertEqual(result, True)

        result = LoginService().exist_email("xxx")

        self.assertEqual(result, False)

    # def test_send_login_url(self):
    # メールが送信されるので書かない。

    def test_get_active_user_case1(self):

        MasterData.objects.create(
            code="003",
            sub_code="01",
            value='15',
            sub_value='sub_value',
            comment='')

        result = LoginService().get_active_user(None)
        self.assertEqual(result, None)

    def test_get_active_user_case2(self):

        MasterData.objects.create(
            code="002",
            sub_code="01",
            value='active',
            sub_value='sub_value',
            comment='')

        MasterData.objects.create(
            code="003",
            sub_code="01",
            value='15',
            sub_value='sub_value',
            comment='')

        ApplicationUserRepository().insert(
            "U0002",
            "email@example.com",
            "first_name2",
            "last_name2",
            "full_name2",
            "01",
            "01",
            "comment2",
            "U0001")

        ApplicationUserRepository().insert(
            "U0003",
            "email3@example.com",
            "first_name3",
            "last_name3",
            "full_name3",
            "02",
            "02",
            "comment3",
            "U0001")

        request_email = "email@example.com"
        onetime_password = get_random_string(200)

        TemporarilyLoginUrlRepository().insert(request_email, onetime_password)

        result = LoginService().get_active_user(onetime_password)

        self.assertEqual(result.user_id, "U0002")
        self.assertEqual(result.email, "email@example.com")
        self.assertEqual(result.first_name, "first_name2")
        self.assertEqual(result.last_name, "last_name2")
        self.assertEqual(result.full_name, "full_name2")
        self.assertEqual(result.authority, "01")
        self.assertEqual(result.status, "01")
        self.assertEqual(result.comment, "comment2")
        self.assertEqual(result.create_user_id, "U0001")
        self.assertEqual(result.update_user_id, "U0001")

        result = LoginService().get_active_user('onetime_password')

        self.assertEqual(result, None)
