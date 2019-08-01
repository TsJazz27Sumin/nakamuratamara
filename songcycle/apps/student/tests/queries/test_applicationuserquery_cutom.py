from django.test import TestCase
from datetime import datetime

from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.models.applicationuser import ApplicationUser
from apps.student.models.masterdata import MasterData


class ApplicationUserQueryCustomTestCase(TestCase):

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

        ApplicationUser.objects.create(
            user_id='U0001',
            email='example1.com',
            first_name='first_name1',
            last_name='last_name1',
            full_name='first_name1 last_name1',
            authority='01',
            status='03',
            first_login_date_timestamp=datetime.now(),
            last_login_date_timestamp=datetime.now(),
            login_count=1,
            comment='comment1',
            create_user_id='S0001',
            create_timestamp=datetime.now(),
            update_user_id='S0001',
            update_timestamp=datetime.now()
        )

        ApplicationUser.objects.create(
            user_id='U0002',
            email='example2.com',
            first_name='first_name2',
            last_name='last_name2',
            full_name='first_name2 last_name2',
            authority='01',
            status='02',
            first_login_date_timestamp=datetime.now(),
            last_login_date_timestamp=datetime.now(),
            login_count=1,
            comment='comment2',
            create_user_id='S0001',
            create_timestamp=datetime.now(),
            update_user_id='S0001',
            update_timestamp=datetime.now()
        )

        ApplicationUser.objects.create(
            user_id='U0003',
            email='example3.com',
            first_name='first_name3',
            last_name='last_name3',
            full_name='first_name3 last_name3',
            authority='01',
            status='03',
            first_login_date_timestamp=datetime.now(),
            last_login_date_timestamp=datetime.now(),
            login_count=1,
            comment='comment3',
            create_user_id='S0001',
            create_timestamp=datetime.now(),
            update_user_id='S0001',
            update_timestamp=datetime.now()
        )

    def test_custom_count_case1(self):
            
        result = ApplicationUserQuery().custom_count('xample', 'name')
        self.assertEqual(result, 3)

    def test_custom_count_case2(self):
            
        result = ApplicationUserQuery().custom_count('aaa', 'name')
        self.assertEqual(result, 0)

    def test_custom_count_case3(self):
            
        result = ApplicationUserQuery().custom_count('xample', 'aaa')
        self.assertEqual(result, 0)

    def test_custom_count_case4(self):
            
        result = ApplicationUserQuery().custom_count('aaa', 'aaa')
        self.assertEqual(result, 0)

    def test_custom_count_case5(self):
            
        result = ApplicationUserQuery().custom_count('xample1', '')
        self.assertEqual(result, 1)

    def test_custom_count_case6(self):
            
        result = ApplicationUserQuery().custom_count('', '_name1')
        self.assertEqual(result, 1)

    def test_custom_count_case7(self):
            
        result = ApplicationUserQuery().custom_count('', '')
        self.assertEqual(result, 3)

    def test_custom_query_case1(self):
            
        result_list = ApplicationUserQuery().custom_query('xample', 'name', 0, 10, 'user-id-sort', 'False')
        self.assertEqual(result_list[0].user_id, 'U0001')
        self.assertEqual(result_list[0].email, 'example1.com')
        self.assertEqual(result_list[0].full_name, 'first_name1 last_name1')
        self.assertEqual(result_list[0].authority, '01')
        self.assertEqual(result_list[0].status, '03')
        self.assertEqual(result_list[0].login_count, 1)

        self.assertEqual(result_list[1].user_id, 'U0002')
        self.assertEqual(result_list[1].email, 'example2.com')
        self.assertEqual(result_list[1].full_name, 'first_name2 last_name2')
        self.assertEqual(result_list[1].authority, '01')
        self.assertEqual(result_list[1].status, '02')
        self.assertEqual(result_list[1].login_count, 1)

        self.assertEqual(result_list[2].user_id, 'U0003')
        self.assertEqual(result_list[2].email, 'example3.com')
        self.assertEqual(result_list[2].full_name, 'first_name3 last_name3')
        self.assertEqual(result_list[2].authority, '01')
        self.assertEqual(result_list[2].status, '03')
        self.assertEqual(result_list[2].login_count, 1)

    def test_custom_query_case2(self):
            
        result_list = ApplicationUserQuery().custom_query('', '', 0, 10, 'user-id-sort', 'False')
        self.assertEqual(result_list[0].user_id, 'U0001')
        self.assertEqual(result_list[0].email, 'example1.com')
        self.assertEqual(result_list[0].full_name, 'first_name1 last_name1')
        self.assertEqual(result_list[0].authority, '01')
        self.assertEqual(result_list[0].status, '03')
        self.assertEqual(result_list[0].login_count, 1)

        self.assertEqual(result_list[1].user_id, 'U0002')
        self.assertEqual(result_list[1].email, 'example2.com')
        self.assertEqual(result_list[1].full_name, 'first_name2 last_name2')
        self.assertEqual(result_list[1].authority, '01')
        self.assertEqual(result_list[1].status, '02')
        self.assertEqual(result_list[1].login_count, 1)

        self.assertEqual(result_list[2].user_id, 'U0003')
        self.assertEqual(result_list[2].email, 'example3.com')
        self.assertEqual(result_list[2].full_name, 'first_name3 last_name3')
        self.assertEqual(result_list[2].authority, '01')
        self.assertEqual(result_list[2].status, '03')
        self.assertEqual(result_list[2].login_count, 1)

    def test_custom_query_case3(self):
            
        result_list = ApplicationUserQuery().custom_query('xample1', '', 0, 10, 'user-id-sort', 'False')
        self.assertEqual(result_list[0].user_id, 'U0001')
        self.assertEqual(result_list[0].email, 'example1.com')
        self.assertEqual(result_list[0].full_name, 'first_name1 last_name1')
        self.assertEqual(result_list[0].authority, '01')
        self.assertEqual(result_list[0].status, '03')
        self.assertEqual(result_list[0].login_count, 1)

    def test_custom_query_case4(self):
            
        result_list = ApplicationUserQuery().custom_query('', '_name1', 0, 10, 'user-id-sort', 'False')
        self.assertEqual(result_list[0].user_id, 'U0001')
        self.assertEqual(result_list[0].email, 'example1.com')
        self.assertEqual(result_list[0].full_name, 'first_name1 last_name1')
        self.assertEqual(result_list[0].authority, '01')
        self.assertEqual(result_list[0].status, '03')
        self.assertEqual(result_list[0].login_count, 1)

    def test_custom_query_case5(self):
            
        result_list = ApplicationUserQuery().custom_query('xample1', 'aaa', 0, 10, 'user-id-sort', 'False')
        self.assertEqual(result_list, [])

    def test_custom_query_case6(self):
            
        result_list = ApplicationUserQuery().custom_query('aaa', '_name1', 0, 10, 'user-id-sort', 'False')
        self.assertEqual(result_list, [])

    def test_custom_query_case7(self):
            
        result_list = ApplicationUserQuery().custom_query('aaa', 'aaa', 0, 10, 'user-id-sort', 'False')
        self.assertEqual(result_list, [])

    def test_custom_query_case8(self):
            
        result_list = ApplicationUserQuery().custom_query('', '', 2, 2, 'user-id-sort', 'False')

        self.assertEqual(result_list[0].user_id, 'U0003')
        self.assertEqual(result_list[0].email, 'example3.com')
        self.assertEqual(result_list[0].full_name, 'first_name3 last_name3')
        self.assertEqual(result_list[0].authority, '01')
        self.assertEqual(result_list[0].status, '03')
        self.assertEqual(result_list[0].login_count, 1)

    def test_custom_query_case9(self):
            
        result_list = ApplicationUserQuery().custom_query('', '', 2, 2, 'user-id-sort', 'True')

        self.assertEqual(result_list[0].user_id, 'U0001')
        self.assertEqual(result_list[0].email, 'example1.com')
        self.assertEqual(result_list[0].full_name, 'first_name1 last_name1')
        self.assertEqual(result_list[0].authority, '01')
        self.assertEqual(result_list[0].status, '03')
        self.assertEqual(result_list[0].login_count, 1)
