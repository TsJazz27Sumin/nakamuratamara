from django.test import TestCase

from apps.student.functions import function


class FunctionTestCase(TestCase):

    def test_get_value_case1(self):

        result = function.get_value('value', 'default_value')
        self.assertEqual(result, 'value')

    def test_get_value_case2(self):

        result = function.get_value(None, 'default_value')
        self.assertEqual(result, 'default_value')

    def test_get_offset_case1(self):

        previous = True
        next = False
        target_page = 0
        current_page = 2
        limit = 2

        offset, target_page = function.get_offset(
            previous, next, target_page, current_page, limit)

        self.assertEqual(offset, 0)
        self.assertEqual(target_page, 1)

    def test_get_offset_case2(self):
    
        previous = False
        next = True
        target_page = 0
        current_page = 1
        limit = 2

        offset, target_page = function.get_offset(
            previous, next, target_page, current_page, limit)

        self.assertEqual(offset, 2)
        self.assertEqual(target_page, 2)

    def test_get_offset_case3(self):
        
        previous = False
        next = False
        target_page = 2
        current_page = 1
        limit = 2

        offset, target_page = function.get_offset(
            previous, next, target_page, current_page, limit)

        self.assertEqual(offset, 2)
        self.assertEqual(target_page, 2)
