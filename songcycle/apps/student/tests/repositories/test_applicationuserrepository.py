from django.test import TestCase

from apps.student.repositories.applicationuserrepository import ApplicationUserRepository
from apps.student.queries.applicationuserquery import ApplicationUserQuery


class ApplicationUserRepositoryTestCase(TestCase):

    def test(self):

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

        self.assertEqual(user.email, "email@example.com")
        self.assertEqual(user.first_name, "first_name")
        self.assertEqual(user.last_name, "last_name")
        self.assertEqual(user.full_name, "full_name")
        self.assertEqual(user.authority, "01")
        self.assertEqual(user.status, "02")
        self.assertEqual(user.comment, "comment")
        self.assertEqual(user.create_user_id, "U0001")
        self.assertEqual(user.update_user_id, "U0001")

        user.email = "email3@example.com"
        user.first_name = "first_name3"
        user.last_name = "last_name3"
        user.full_name = "full_name3"
        user.authority = "03"
        user.status = "04"
        user.comment = "comment3"
        user.update_user_id = "U0003"

        ApplicationUserRepository().update(user)

        result = ApplicationUserQuery().get_user("U0002")

        self.assertEqual(result.email, "email3@example.com")
        self.assertEqual(result.first_name, "first_name3")
        self.assertEqual(result.last_name, "last_name3")
        self.assertEqual(result.full_name, "full_name3")
        self.assertEqual(result.authority, "03")
        self.assertEqual(result.status, "04")
        self.assertEqual(result.comment, "comment3")
        self.assertEqual(result.create_user_id, "U0001")
        self.assertEqual(result.update_user_id, "U0003")

        ApplicationUserRepository().delete(result)

        deleted = ApplicationUserQuery().get_user("U0002")

        self.assertEqual(deleted, None)

