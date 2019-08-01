from django.test import TestCase
from datetime import datetime, timedelta

from apps.student.queries.reportquery import ReportQuery
from apps.student.models.report import Report
from apps.student.models.applicationuser import ApplicationUser
from apps.student.models.downloadinformation import DownloadInformation


class ReportQueryTestCase(TestCase):

    def setUp(self):
        Report.objects.create(
            report_id="R000001",
            auther_user_id="U0001",
            target_year="2019",
            file_name="file_name001",
            google_file_id="google_file_id_001",
            comment="comment001",
            create_user_id="U0001",
            create_timestamp=datetime.now() - timedelta(minutes=10),
            update_user_id="U0001",
            update_timestamp=datetime.now() - timedelta(minutes=10)
        )
        Report.objects.create(
            report_id="R000002",
            auther_user_id="U0002",
            target_year="2019",
            file_name="file_name002",
            google_file_id="google_file_id_002",
            comment="comment002",
            create_user_id="U0001",
            create_timestamp=datetime.now() - timedelta(minutes=5),
            update_user_id="U0001",
            update_timestamp=datetime.now() - timedelta(minutes=5)
        )
        Report.objects.create(
            report_id="R000003",
            auther_user_id="U0001",
            target_year="2018",
            file_name="file_name003",
            google_file_id="google_file_id_003",
            comment="comment003",
            create_user_id="U0001",
            create_timestamp=datetime.now() - timedelta(minutes=10),
            update_user_id="U0001",
            update_timestamp=datetime.now() - timedelta(minutes=10)
        )
        Report.objects.create(
            report_id="R000004",
            auther_user_id="U0002",
            target_year="2018",
            file_name="file_name004",
            google_file_id="google_file_id_004",
            comment="comment004",
            create_user_id="U0001",
            create_timestamp=datetime.now() - timedelta(minutes=5),
            update_user_id="U0001",
            update_timestamp=datetime.now() - timedelta(minutes=5)
        )

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

        DownloadInformation.objects.create(
            report_id="R000001",
            user_id="U0001"
        )
        DownloadInformation.objects.create(
            report_id="R000001",
            user_id="U0002"
        )
        DownloadInformation.objects.create(
            report_id="R000002",
            user_id="U0001"
        )
        DownloadInformation.objects.create(
            report_id="R000002",
            user_id="U0002"
        )

    def test_select_all_case1(self):

        result_list = ReportQuery().select_all()
        self.assertEqual(len(result_list), 4)

        self.assertEqual(result_list[0].report_id, "R000002")
        self.assertEqual(result_list[0].auther_user_id, "U0002")
        self.assertEqual(result_list[0].target_year, "2019")
        self.assertEqual(result_list[0].file_name, "file_name002")
        self.assertEqual(result_list[0].google_file_id, "google_file_id_002")
        self.assertEqual(result_list[0].comment, "comment002")
        self.assertEqual(result_list[0].create_user_id, "U0001")
        self.assertEqual(result_list[0].update_user_id, "U0001")

        self.assertEqual(result_list[1].report_id, "R000001")
        self.assertEqual(result_list[1].auther_user_id, "U0001")
        self.assertEqual(result_list[1].target_year, "2019")
        self.assertEqual(result_list[1].file_name, "file_name001")
        self.assertEqual(result_list[1].google_file_id, "google_file_id_001")
        self.assertEqual(result_list[1].comment, "comment001")
        self.assertEqual(result_list[1].create_user_id, "U0001")
        self.assertEqual(result_list[1].update_user_id, "U0001")

        self.assertEqual(result_list[2].report_id, "R000004")
        self.assertEqual(result_list[2].auther_user_id, "U0002")
        self.assertEqual(result_list[2].target_year, "2018")
        self.assertEqual(result_list[2].file_name, "file_name004")
        self.assertEqual(result_list[2].google_file_id, "google_file_id_004")
        self.assertEqual(result_list[2].comment, "comment004")
        self.assertEqual(result_list[2].create_user_id, "U0001")
        self.assertEqual(result_list[2].update_user_id, "U0001")

        self.assertEqual(result_list[3].report_id, "R000003")
        self.assertEqual(result_list[3].auther_user_id, "U0001")
        self.assertEqual(result_list[3].target_year, "2018")
        self.assertEqual(result_list[3].file_name, "file_name003")
        self.assertEqual(result_list[3].google_file_id, "google_file_id_003")
        self.assertEqual(result_list[3].comment, "comment003")
        self.assertEqual(result_list[3].create_user_id, "U0001")
        self.assertEqual(result_list[3].update_user_id, "U0001")

    def test_get_one_case1(self):
    
        result = ReportQuery().get_one('R000002')

        self.assertEqual(result.report_id, "R000002")
        self.assertEqual(result.auther_user_id, "U0002")
        self.assertEqual(result.target_year, "2019")
        self.assertEqual(result.file_name, "file_name002")
        self.assertEqual(result.google_file_id, "google_file_id_002")
        self.assertEqual(result.comment, "comment002")
        self.assertEqual(result.create_user_id, "U0001")
        self.assertEqual(result.update_user_id, "U0001")

    def test_exist_same_file_name_case1(self):
        
        result = ReportQuery().exist_same_file_name("file_name002")

        self.assertEqual(result, True)

    def test_exist_same_file_name_case2(self):
        
        result = ReportQuery().exist_same_file_name("abc")

        self.assertEqual(result, False)
