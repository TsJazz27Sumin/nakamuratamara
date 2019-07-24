from django.test import TestCase
from datetime import datetime, timedelta

from apps.student.queries.temporarilyloginurlquery import TemporarilyLoginUrlQuery
from apps.student.models.temporarilyloginurl import TemporarilyLoginUrl


class TemporarilyLoginUrlQueryTestCase(TestCase):

    def setUp(self):
        TemporarilyLoginUrl.objects.create(onetime_password='pwd')

    def test_is_valid_onetime_password_case1(self):

        valid_time = datetime.now() - timedelta(minutes=15)
    
        result = TemporarilyLoginUrlQuery().is_valid_onetime_password('pwd', valid_time)
        self.assertEqual(result is not None, True)

    def test_is_valid_onetime_password_case2(self):
    
        valid_time = datetime.now() + timedelta(minutes=15)
    
        result = TemporarilyLoginUrlQuery().is_valid_onetime_password('pwd', valid_time)
        self.assertEqual(result is not None, False)

    def test_is_valid_onetime_password_case3(self):
    
        valid_time = datetime.now() - timedelta(minutes=15)
    
        result = TemporarilyLoginUrlQuery().is_valid_onetime_password('error', valid_time)
        self.assertEqual(result is not None, False)

    def test_is_valid_onetime_password_case4(self):
        
        valid_time = datetime.now() + timedelta(minutes=15)
    
        result = TemporarilyLoginUrlQuery().is_valid_onetime_password('error', valid_time)
        self.assertEqual(result is not None, False)
