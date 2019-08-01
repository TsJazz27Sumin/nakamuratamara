from django.test import TestCase

from apps.student.templatetags import lookup


class LookupTestCase(TestCase):

    def test_lookup_case1(self):

        result = lookup.lookup({'key': 'value'}, 'key', 'default_value')
        self.assertEqual(result, 'value')

    def test_lookup_case2(self):
    
        result = lookup.lookup({'key': 'value'}, 'abc', 'default_value')
        self.assertEqual(result, 'default_value')
