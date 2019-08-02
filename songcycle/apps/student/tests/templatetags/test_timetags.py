from django.test import TestCase
from datetime import datetime

from apps.student.templatetags import timetags


class TimetagsTestCase(TestCase):

    def test_to_jst_case1(self):

        result = timetags.to_jst(datetime.now())
        self.assertEqual(result, datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    def test_to_jst_case2(self):
    
        result = timetags.to_jst(None)
        self.assertEqual(result, '')
