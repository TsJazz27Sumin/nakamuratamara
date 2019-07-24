from django.test import TestCase

from apps.student.queries.masterquery import MasterQuery
from apps.student.models.masterdata import MasterData


class MasterQueryTestCase(TestCase):

    def setUp(self):
        MasterData.objects.create(
            code="001",
            sub_code="01",
            value='value1',
            sub_value='sub_value',
            comment='')
        MasterData.objects.create(
            code="001",
            sub_code="02",
            value='value2',
            sub_value='sub_value',
            comment='')
        MasterData.objects.create(
            code="002",
            sub_code="01",
            value='value3',
            sub_value='sub_value',
            comment='')
        MasterData.objects.create(
            code="002",
            sub_code="02",
            value='value4',
            sub_value='sub_value',
            comment='')
        MasterData.objects.create(
            code="002",
            sub_code="03",
            value='active',
            sub_value='sub_value',
            comment='')
        MasterData.objects.create(
            code="003",
            sub_code="01",
            value='15',
            sub_value='sub_value',
            comment='')
        MasterData.objects.create(
            code="004",
            sub_code="01",
            value='url',
            sub_value='sub_value',
            comment='')
        MasterData.objects.create(
            code="005",
            sub_code="01",
            value='event_type',
            sub_value='sub_value',
            comment='')

    def test_get_value_case1(self):

        result = MasterQuery().get_value('00101')
        self.assertEqual(result, 'value1')

    def test_get_value_case2(self):

        result = MasterQuery().get_value('001011')
        self.assertEqual(result, None)

    def test_get_authority_value(self):

        result = MasterQuery().get_authority_value('01')
        self.assertEqual(result, 'value1')

    def test_get_authority_dictionary(self):

        result = MasterQuery().get_authority_dictionary()
        self.assertEqual(result, {'01': 'value1', '02': 'value2'})

    def test_get_user_status_dictionary(self):

        result = MasterQuery().get_user_status_dictionary()
        self.assertEqual(
            result, {
                '01': 'value3', '02': 'value4', '03': 'active'})

    def test_get_authority_taples(self):

        result = MasterQuery().get_authority_taples()
        self.assertEqual(result, [('01', 'value1'), ('02', 'value2')])

    def test_get_user_status_taples(self):

        result = MasterQuery().get_user_status_taples()
        self.assertEqual(
            result, [
                ('01', 'value3'), ('02', 'value4'), ('03', 'active')])

    def test_get_active_user_status_sub_code(self):

        result = MasterQuery().get_active_user_status_sub_code()
        self.assertEqual(result, '03')

    def test_get_temporary_time(self):

        result = MasterQuery().get_temporary_time()
        self.assertEqual(result, 15)

    def test_get_root_login_url(self):

        result = MasterQuery().get_root_login_url()
        self.assertEqual(result, 'url')

    def test_get_event_type_request_login(self):

        result = MasterQuery().get_event_type_request_login()
        self.assertEqual(result, 'event_type')
