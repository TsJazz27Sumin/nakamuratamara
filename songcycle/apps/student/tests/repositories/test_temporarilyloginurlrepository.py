from django.test import TestCase
from datetime import datetime, timedelta
from django.utils.crypto import get_random_string

from apps.student.repositories.temporarilyloginurlrepository import TemporarilyLoginUrlRepository
from apps.student.queries.temporarilyloginurlquery import TemporarilyLoginUrlQuery


class TemporarilyLoginUrlRepositoryTestCase(TestCase):

    def test(self):

        request_email = "example.com"
        onetime_password = get_random_string(200)

        TemporarilyLoginUrlRepository().insert(request_email, onetime_password)

        valid_time = datetime.now() - timedelta(minutes=15)

        result = TemporarilyLoginUrlQuery().is_valid_onetime_password(
            onetime_password, valid_time)

        self.assertEqual(result.request_email, request_email)
