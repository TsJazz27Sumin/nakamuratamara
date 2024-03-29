from django.test import TestCase
from datetime import datetime

from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.models.applicationuser import ApplicationUser
from apps.student.models.masterdata import MasterData


class ApplicationUserQueryTestCase(TestCase):

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

    def test_is_active_user_case1(self):
    
        result = ApplicationUserQuery().is_active_user('example1.com')
        self.assertEqual(result, True)

    def test_is_active_user_case2(self):
        
        result = ApplicationUserQuery().is_active_user('example2.com')
        self.assertEqual(result, False)

    def test_is_exist_user_case1(self):
        
        result = ApplicationUserQuery().is_exist_user('U0001')
        self.assertEqual(result, True)

    def test_is_exist_user_case2(self):
        
        result = ApplicationUserQuery().is_exist_user('U9999')
        self.assertEqual(result, False)

    def test_is_exist_same_email_case1(self):
        
        result = ApplicationUserQuery().is_exist_same_email('example1.com')
        self.assertEqual(result, True)

    def test_is_exist_same_email_case2(self):
        
        result = ApplicationUserQuery().is_exist_same_email('example999.com')
        self.assertEqual(result, False)

    def test_is_exist_same_full_name_case1(self):
        
        result = ApplicationUserQuery().is_exist_same_full_name('first_name1 last_name1')
        self.assertEqual(result, True)

    def test_is_exist_same_full_name_case2(self):
        
        result = ApplicationUserQuery().is_exist_same_full_name('first_name9 last_name9')
        self.assertEqual(result, False)
    
    def test_get_active_user_case1(self):
            
        result = ApplicationUserQuery().get_active_user('example1.com')
        self.assertEqual(result.user_id, 'U0001')
        self.assertEqual(result.email, 'example1.com')
        self.assertEqual(result.first_name, 'first_name1')
        self.assertEqual(result.last_name, 'last_name1')
        self.assertEqual(result.full_name, 'first_name1 last_name1')
        self.assertEqual(result.authority, '01')
        self.assertEqual(result.status, '03')
        self.assertEqual(result.login_count, 1)
        self.assertEqual(result.comment, 'comment1')
        self.assertEqual(result.create_user_id, 'S0001')
        self.assertEqual(result.update_user_id, 'S0001')

    def test_get_active_user_case2(self):
        
        result = ApplicationUserQuery().get_active_user('example999.com')
        self.assertEqual(result, None)

    def test_get_active_users_case1(self):
            
        result_list = ApplicationUserQuery().get_active_users()

        self.assertEqual(result_list[0].user_id, 'U0001')
        self.assertEqual(result_list[0].email, 'example1.com')
        self.assertEqual(result_list[0].first_name, 'first_name1')
        self.assertEqual(result_list[0].last_name, 'last_name1')
        self.assertEqual(result_list[0].full_name, 'first_name1 last_name1')
        self.assertEqual(result_list[0].authority, '01')
        self.assertEqual(result_list[0].status, '03')
        self.assertEqual(result_list[0].login_count, 1)
        self.assertEqual(result_list[0].comment, 'comment1')
        self.assertEqual(result_list[0].create_user_id, 'S0001')
        self.assertEqual(result_list[0].update_user_id, 'S0001')

        self.assertEqual(result_list[1].user_id, 'U0003')
        self.assertEqual(result_list[1].email, 'example3.com')
        self.assertEqual(result_list[1].first_name, 'first_name3')
        self.assertEqual(result_list[1].last_name, 'last_name3')
        self.assertEqual(result_list[1].full_name, 'first_name3 last_name3')
        self.assertEqual(result_list[1].authority, '01')
        self.assertEqual(result_list[1].status, '03')
        self.assertEqual(result_list[1].login_count, 1)
        self.assertEqual(result_list[1].comment, 'comment3')
        self.assertEqual(result_list[1].create_user_id, 'S0001')
        self.assertEqual(result_list[1].update_user_id, 'S0001')

    def test_get_user_case1(self):
            
        result = ApplicationUserQuery().get_user('U0001')
        self.assertEqual(result.user_id, 'U0001')
        self.assertEqual(result.email, 'example1.com')
        self.assertEqual(result.first_name, 'first_name1')
        self.assertEqual(result.last_name, 'last_name1')
        self.assertEqual(result.full_name, 'first_name1 last_name1')
        self.assertEqual(result.authority, '01')
        self.assertEqual(result.status, '03')
        self.assertEqual(result.login_count, 1)
        self.assertEqual(result.comment, 'comment1')
        self.assertEqual(result.create_user_id, 'S0001')
        self.assertEqual(result.update_user_id, 'S0001')

    def test_get_user_case2(self):
        
        result = ApplicationUserQuery().get_user('example999.com')
        self.assertEqual(result, None)
