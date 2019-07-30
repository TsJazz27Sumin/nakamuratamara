from django.test import TestCase
from datetime import datetime, timedelta

from apps.student.queries.accessinformationquery import AccessInformationQuery
from apps.student.models.accessinformation import AccessInformation


class AccessInformationQueryTestCase(TestCase):

    def setUp(self):
        AccessInformation.objects.create(
            event_type='event_type1',
            http_accept_language='http_accept_language',
            browser='browser',
            browser_version='browser_version',
            os='os',
            os_version='os_version',
            device='device',
            device_brand='device_brand',
            device_type='device_type',
            remote_addr='remote_addr',
            access_date=datetime.now(),
            access_date_timestamp=datetime.now() - timedelta(minutes=5),
            success_value='',
            fault_value='fault_value',
            comment='comment'
        )
        AccessInformation.objects.create(
            event_type='event_type2',
            http_accept_language='http_accept_language',
            browser='browser',
            browser_version='browser_version',
            os='os',
            os_version='os_version',
            device='device',
            device_brand='device_brand',
            device_type='device_type',
            remote_addr='remote_addr',
            access_date=datetime.now(),
            access_date_timestamp=datetime.now() - timedelta(minutes=6),
            success_value='',
            fault_value='fault_value',
            comment='comment'
        )
        AccessInformation.objects.create(
            event_type='event_type3',
            http_accept_language='http_accept_language',
            browser='browser',
            browser_version='browser_version',
            os='os',
            os_version='os_version',
            device='device',
            device_brand='device_brand',
            device_type='device_type',
            remote_addr='remote_addr',
            access_date=datetime.now(),
            access_date_timestamp=datetime.now() - timedelta(minutes=7),
            success_value='',
            fault_value='',
            comment='comment'
        )
        AccessInformation.objects.create(
            event_type='event_type4',
            http_accept_language='http_accept_language',
            browser='browser',
            browser_version='browser_version',
            os='os',
            os_version='os_version',
            device='device',
            device_brand='device_brand',
            device_type='device_type',
            remote_addr='xxx',
            access_date=datetime.now(),
            access_date_timestamp=datetime.now() - timedelta(minutes=8),
            success_value='',
            fault_value='fault_value',
            comment='comment'
        )

    def test_get_fault_count(self):
        result = AccessInformationQuery().get_fault_count('remote_addr', datetime.now())
        self.assertEqual(result, 2)

    def test_select_all(self):
        result_list = AccessInformationQuery().select_all()
        self.assertEqual(len(result_list), 4)

        self.assertEqual(result_list[0].event_type, 'event_type1')
        self.assertEqual(result_list[1].event_type, 'event_type2')
        self.assertEqual(result_list[2].event_type, 'event_type3')
        self.assertEqual(result_list[3].event_type, 'event_type4')
            
