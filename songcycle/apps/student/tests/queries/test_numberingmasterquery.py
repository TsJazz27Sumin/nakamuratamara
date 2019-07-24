from django.test import TestCase

from apps.student.queries.numberingmasterquery import NumberingMasterQuery
from apps.student.models.numberingmaster import NumberingMaster


class NumberingMasterQueryTestCase(TestCase):

    def setUp(self):
        NumberingMaster.objects.create(
            code='01', initial='U', value=1, comment='')
        NumberingMaster.objects.create(
            code='02', initial='R', value=1, comment='')

    def test_get_report_id(self):
    
        result = NumberingMasterQuery().get_report_id()
        self.assertEqual(result, 'R000001')

    def test_get_user_id(self):
        
        result = NumberingMasterQuery().get_user_id()
        self.assertEqual(result, 'U0001')

