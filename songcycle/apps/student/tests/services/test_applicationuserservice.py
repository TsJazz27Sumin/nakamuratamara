from django.test import TestCase

from apps.student.services.applicationuserservice import ApplicationUserService
from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.models.numberingmaster import NumberingMaster
from apps.student.models.masterdata import MasterData


class ApplicationUserServiceTestCase(TestCase):

    def setUp(self):
        NumberingMaster.objects.create(
            code='01', initial='U', value=1, comment='')
        NumberingMaster.objects.create(
            code='02', initial='R', value=1, comment='')
        MasterData.objects.create(
            code="002",
            sub_code="01",
            value='active',
            sub_value='sub_value',
            comment='')
        MasterData.objects.create(
            code="002",
            sub_code="02",
            value='stop',
            sub_value='sub_value',
            comment='')

    def test(self):

        user_id = ""
        email = "email@example.com"
        first_name = "first_name"
        last_name = "last_name"
        full_name = "full_name"
        authority = "02"
        status = "01"
        comment = "comment"
        login_user_id = "U0000"

        ApplicationUserService().save_user(
            user_id,
            email,
            first_name,
            last_name,
            full_name,
            authority,
            status,
            comment,
            login_user_id)

        user_list = ApplicationUserQuery().get_active_users()
        user = user_list[0]

        self.assertEqual(user.email, "email@example.com")
        self.assertEqual(user.first_name, "first_name")
        self.assertEqual(user.last_name, "last_name")
        self.assertEqual(user.full_name, "full_name")
        self.assertEqual(user.authority, "02")
        self.assertEqual(user.status, "01")
        self.assertEqual(user.comment, "comment")
        self.assertEqual(user.create_user_id, "U0000")
        self.assertEqual(user.update_user_id, "U0000")

        user_id = user.user_id
        email = "email3@example.com"
        first_name = "first_name3"
        last_name = "last_name3"
        full_name = "full_name3"
        authority = "03"
        status = "02"
        comment = "comment3"
        login_user_id = "U0003"

        ApplicationUserService().save_user(
            user_id,
            email,
            first_name,
            last_name,
            full_name,
            authority,
            status,
            comment,
            login_user_id)

        result = ApplicationUserQuery().get_user(user_id)

        self.assertEqual(result.email, "email3@example.com")
        self.assertEqual(result.first_name, "first_name3")
        self.assertEqual(result.last_name, "last_name3")
        self.assertEqual(result.full_name, "full_name3")
        self.assertEqual(result.authority, "03")
        self.assertEqual(result.status, "02")
        self.assertEqual(result.comment, "comment3")
        self.assertEqual(result.create_user_id, "U0000")
        self.assertEqual(result.update_user_id, "U0003")

        ApplicationUserService().delete_user(user_id)

        deleted = ApplicationUserQuery().get_user(user_id)

        self.assertEqual(deleted, None)

