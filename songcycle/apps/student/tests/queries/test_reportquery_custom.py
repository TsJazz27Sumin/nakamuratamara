from django.test import TestCase
from datetime import datetime, timedelta

from apps.student.queries.reportquery import ReportQuery
from apps.student.models.report import Report
from apps.student.models.applicationuser import ApplicationUser
from apps.student.models.downloadinformation import DownloadInformation


class ReportQueryCustomTestCase(TestCase):

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
            create_timestamp=datetime.now() - timedelta(minutes=9),
            update_user_id="U0001",
            update_timestamp=datetime.now() - timedelta(minutes=9)
        )
        Report.objects.create(
            report_id="R000003",
            auther_user_id="U0001",
            target_year="2018",
            file_name="file_name003",
            google_file_id="google_file_id_003",
            comment="comment003",
            create_user_id="U0001",
            create_timestamp=datetime.now() - timedelta(minutes=8),
            update_user_id="U0001",
            update_timestamp=datetime.now() - timedelta(minutes=8)
        )
        Report.objects.create(
            report_id="R000004",
            auther_user_id="U0002",
            target_year="2018",
            file_name="file_name004",
            google_file_id="google_file_id_004",
            comment="comment004",
            create_user_id="U0001",
            create_timestamp=datetime.now() - timedelta(minutes=7),
            update_user_id="U0001",
            update_timestamp=datetime.now() - timedelta(minutes=7)
        )
        Report.objects.create(
            report_id="R000005",
            auther_user_id="U0002",
            target_year="2017",
            file_name="file_xxxx005",
            google_file_id="google_file_id_005",
            comment="comment005",
            create_user_id="U0001",
            create_timestamp=datetime.now() - timedelta(minutes=6),
            update_user_id="U0001",
            update_timestamp=datetime.now() - timedelta(minutes=6)
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

    def test_custom_count_case1(self):
        
        result = ReportQuery().custom_count("2019", "", "")

        self.assertEqual(result, 2)

    def test_custom_count_case2(self):
        
        result = ReportQuery().custom_count("", "_name1", "")

        self.assertEqual(result, 2)

    def test_custom_count_case3(self):
        
        result = ReportQuery().custom_count("", "", "_name")

        self.assertEqual(result, 4)

    def test_custom_count_case4(self):
        
        result = ReportQuery().custom_count("2019", "_name1", "_name")

        self.assertEqual(result, 1)

    def test_custom_query_case1(self):
        
        result_list = ReportQuery().custom_query("", "", "", 0, 5, "target-year-sort", "True")

        self.assertEqual(len(result_list), 5)

        self.assertEqual(result_list[0].report_id, "R000002")
        self.assertEqual(result_list[0].target_year, "2019")
        self.assertEqual(result_list[0].file_name, "file_name002")
        self.assertEqual(result_list[0].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[0].download_count, 2)
        self.assertEqual(result_list[0].comment, "comment002")

        self.assertEqual(result_list[1].report_id, "R000001")
        self.assertEqual(result_list[1].target_year, "2019")
        self.assertEqual(result_list[1].file_name, "file_name001")
        self.assertEqual(result_list[1].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[1].download_count, 2)
        self.assertEqual(result_list[1].comment, "comment001")

        self.assertEqual(result_list[2].report_id, "R000004")
        self.assertEqual(result_list[2].target_year, "2018")
        self.assertEqual(result_list[2].file_name, "file_name004")
        self.assertEqual(result_list[2].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[2].download_count, 0)
        self.assertEqual(result_list[2].comment, "comment004")

        self.assertEqual(result_list[3].report_id, "R000003")
        self.assertEqual(result_list[3].target_year, "2018")
        self.assertEqual(result_list[3].file_name, "file_name003")
        self.assertEqual(result_list[3].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[3].download_count, 0)
        self.assertEqual(result_list[3].comment, "comment003")

        self.assertEqual(result_list[4].report_id, "R000005")
        self.assertEqual(result_list[4].target_year, "2017")
        self.assertEqual(result_list[4].file_name, "file_xxxx005")
        self.assertEqual(result_list[4].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[4].download_count, 0)
        self.assertEqual(result_list[4].comment, "comment005")

    def test_custom_query_case2(self):
        
        result_list = ReportQuery().custom_query("2019", "", "", 0, 5, "target-year-sort", "True")

        self.assertEqual(len(result_list), 2)

        self.assertEqual(result_list[0].report_id, "R000002")
        self.assertEqual(result_list[0].target_year, "2019")
        self.assertEqual(result_list[0].file_name, "file_name002")
        self.assertEqual(result_list[0].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[0].download_count, 2)
        self.assertEqual(result_list[0].comment, "comment002")

        self.assertEqual(result_list[1].report_id, "R000001")
        self.assertEqual(result_list[1].target_year, "2019")
        self.assertEqual(result_list[1].file_name, "file_name001")
        self.assertEqual(result_list[1].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[1].download_count, 2)
        self.assertEqual(result_list[1].comment, "comment001")

    def test_custom_query_case3(self):
        
        result_list = ReportQuery().custom_query("", "_name2", "", 0, 5, "target-year-sort", "True")

        self.assertEqual(len(result_list), 3)

        self.assertEqual(result_list[0].report_id, "R000002")
        self.assertEqual(result_list[0].target_year, "2019")
        self.assertEqual(result_list[0].file_name, "file_name002")
        self.assertEqual(result_list[0].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[0].download_count, 2)
        self.assertEqual(result_list[0].comment, "comment002")

        self.assertEqual(result_list[1].report_id, "R000004")
        self.assertEqual(result_list[1].target_year, "2018")
        self.assertEqual(result_list[1].file_name, "file_name004")
        self.assertEqual(result_list[1].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[1].download_count, 0)
        self.assertEqual(result_list[1].comment, "comment004")

        self.assertEqual(result_list[2].report_id, "R000005")
        self.assertEqual(result_list[2].target_year, "2017")
        self.assertEqual(result_list[2].file_name, "file_xxxx005")
        self.assertEqual(result_list[2].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[2].download_count, 0)
        self.assertEqual(result_list[2].comment, "comment005")

    def test_custom_query_case4(self):
        
        result_list = ReportQuery().custom_query("", "", "_name", 0, 5, "target-year-sort", "True")

        self.assertEqual(len(result_list), 4)

        self.assertEqual(result_list[0].report_id, "R000002")
        self.assertEqual(result_list[0].target_year, "2019")
        self.assertEqual(result_list[0].file_name, "file_name002")
        self.assertEqual(result_list[0].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[0].download_count, 2)
        self.assertEqual(result_list[0].comment, "comment002")

        self.assertEqual(result_list[1].report_id, "R000001")
        self.assertEqual(result_list[1].target_year, "2019")
        self.assertEqual(result_list[1].file_name, "file_name001")
        self.assertEqual(result_list[1].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[1].download_count, 2)
        self.assertEqual(result_list[1].comment, "comment001")

        self.assertEqual(result_list[2].report_id, "R000004")
        self.assertEqual(result_list[2].target_year, "2018")
        self.assertEqual(result_list[2].file_name, "file_name004")
        self.assertEqual(result_list[2].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[2].download_count, 0)
        self.assertEqual(result_list[2].comment, "comment004")

        self.assertEqual(result_list[3].report_id, "R000003")
        self.assertEqual(result_list[3].target_year, "2018")
        self.assertEqual(result_list[3].file_name, "file_name003")
        self.assertEqual(result_list[3].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[3].download_count, 0)
        self.assertEqual(result_list[3].comment, "comment003")

    def test_custom_query_case5(self):
        
        result_list = ReportQuery().custom_query("", "", "", 4, 4, "target-year-sort", "True")

        self.assertEqual(len(result_list), 1)

        self.assertEqual(result_list[0].report_id, "R000005")
        self.assertEqual(result_list[0].target_year, "2017")
        self.assertEqual(result_list[0].file_name, "file_xxxx005")
        self.assertEqual(result_list[0].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[0].download_count, 0)
        self.assertEqual(result_list[0].comment, "comment005")

    def test_custom_query_case6(self):
        
        result_list = ReportQuery().custom_query("", "", "", 4, 4, "target-year-sort", "False")

        self.assertEqual(len(result_list), 1)

        self.assertEqual(result_list[0].report_id, "R000001")
        self.assertEqual(result_list[0].target_year, "2019")
        self.assertEqual(result_list[0].file_name, "file_name001")
        self.assertEqual(result_list[0].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[0].download_count, 2)
        self.assertEqual(result_list[0].comment, "comment001")

    def test_custom_query_case7(self):
        
        result_list = ReportQuery().custom_query("", "", "_name", 0, 5, "auther-user-sort", "False")

        self.assertEqual(len(result_list), 4)

        self.assertEqual(result_list[0].report_id, "R000003")
        self.assertEqual(result_list[0].target_year, "2018")
        self.assertEqual(result_list[0].file_name, "file_name003")
        self.assertEqual(result_list[0].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[0].download_count, 0)
        self.assertEqual(result_list[0].comment, "comment003")

        self.assertEqual(result_list[1].report_id, "R000001")
        self.assertEqual(result_list[1].target_year, "2019")
        self.assertEqual(result_list[1].file_name, "file_name001")
        self.assertEqual(result_list[1].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[1].download_count, 2)
        self.assertEqual(result_list[1].comment, "comment001")

        self.assertEqual(result_list[2].report_id, "R000004")
        self.assertEqual(result_list[2].target_year, "2018")
        self.assertEqual(result_list[2].file_name, "file_name004")
        self.assertEqual(result_list[2].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[2].download_count, 0)
        self.assertEqual(result_list[2].comment, "comment004")

        self.assertEqual(result_list[3].report_id, "R000002")
        self.assertEqual(result_list[3].target_year, "2019")
        self.assertEqual(result_list[3].file_name, "file_name002")
        self.assertEqual(result_list[3].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[3].download_count, 2)
        self.assertEqual(result_list[3].comment, "comment002")

    def test_custom_query_case8(self):
        
        result_list = ReportQuery().custom_query("", "", "_name", 0, 5, "auther-user-sort", "True")

        self.assertEqual(len(result_list), 4)

        self.assertEqual(result_list[0].report_id, "R000004")
        self.assertEqual(result_list[0].target_year, "2018")
        self.assertEqual(result_list[0].file_name, "file_name004")
        self.assertEqual(result_list[0].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[0].download_count, 0)
        self.assertEqual(result_list[0].comment, "comment004")

        self.assertEqual(result_list[1].report_id, "R000002")
        self.assertEqual(result_list[1].target_year, "2019")
        self.assertEqual(result_list[1].file_name, "file_name002")
        self.assertEqual(result_list[1].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[1].download_count, 2)
        self.assertEqual(result_list[1].comment, "comment002")

        self.assertEqual(result_list[2].report_id, "R000003")
        self.assertEqual(result_list[2].target_year, "2018")
        self.assertEqual(result_list[2].file_name, "file_name003")
        self.assertEqual(result_list[2].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[2].download_count, 0)
        self.assertEqual(result_list[2].comment, "comment003")

        self.assertEqual(result_list[3].report_id, "R000001")
        self.assertEqual(result_list[3].target_year, "2019")
        self.assertEqual(result_list[3].file_name, "file_name001")
        self.assertEqual(result_list[3].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[3].download_count, 2)
        self.assertEqual(result_list[3].comment, "comment001")

    def test_custom_query_case9(self):
        
        result_list = ReportQuery().custom_query("", "", "_name", 0, 5, "file-name-sort", "False")

        self.assertEqual(len(result_list), 4)

        self.assertEqual(result_list[0].report_id, "R000001")
        self.assertEqual(result_list[0].target_year, "2019")
        self.assertEqual(result_list[0].file_name, "file_name001")
        self.assertEqual(result_list[0].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[0].download_count, 2)
        self.assertEqual(result_list[0].comment, "comment001")

        self.assertEqual(result_list[1].report_id, "R000002")
        self.assertEqual(result_list[1].target_year, "2019")
        self.assertEqual(result_list[1].file_name, "file_name002")
        self.assertEqual(result_list[1].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[1].download_count, 2)
        self.assertEqual(result_list[1].comment, "comment002")

        self.assertEqual(result_list[2].report_id, "R000003")
        self.assertEqual(result_list[2].target_year, "2018")
        self.assertEqual(result_list[2].file_name, "file_name003")
        self.assertEqual(result_list[2].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[2].download_count, 0)
        self.assertEqual(result_list[2].comment, "comment003")

        self.assertEqual(result_list[3].report_id, "R000004")
        self.assertEqual(result_list[3].target_year, "2018")
        self.assertEqual(result_list[3].file_name, "file_name004")
        self.assertEqual(result_list[3].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[3].download_count, 0)
        self.assertEqual(result_list[3].comment, "comment004")

    def test_custom_query_case10(self):
        
        result_list = ReportQuery().custom_query("", "", "_name", 0, 5, "download-count-sort", "True")

        self.assertEqual(len(result_list), 4)

        self.assertEqual(result_list[0].report_id, "R000002")
        self.assertEqual(result_list[0].target_year, "2019")
        self.assertEqual(result_list[0].file_name, "file_name002")
        self.assertEqual(result_list[0].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[0].download_count, 2)
        self.assertEqual(result_list[0].comment, "comment002")

        self.assertEqual(result_list[1].report_id, "R000001")
        self.assertEqual(result_list[1].target_year, "2019")
        self.assertEqual(result_list[1].file_name, "file_name001")
        self.assertEqual(result_list[1].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[1].download_count, 2)
        self.assertEqual(result_list[1].comment, "comment001")

        self.assertEqual(result_list[2].report_id, "R000004")
        self.assertEqual(result_list[2].target_year, "2018")
        self.assertEqual(result_list[2].file_name, "file_name004")
        self.assertEqual(result_list[2].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[2].download_count, 0)
        self.assertEqual(result_list[2].comment, "comment004")

        self.assertEqual(result_list[3].report_id, "R000003")
        self.assertEqual(result_list[3].target_year, "2018")
        self.assertEqual(result_list[3].file_name, "file_name003")
        self.assertEqual(result_list[3].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[3].download_count, 0)
        self.assertEqual(result_list[3].comment, "comment003")

    def test_custom_query_case11(self):
        
        result_list = ReportQuery().custom_query("", "", "_name", 0, 5, "download-count-sort", "False")

        self.assertEqual(len(result_list), 4)

        self.assertEqual(result_list[0].report_id, "R000004")
        self.assertEqual(result_list[0].target_year, "2018")
        self.assertEqual(result_list[0].file_name, "file_name004")
        self.assertEqual(result_list[0].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[0].download_count, 0)
        self.assertEqual(result_list[0].comment, "comment004")

        self.assertEqual(result_list[1].report_id, "R000003")
        self.assertEqual(result_list[1].target_year, "2018")
        self.assertEqual(result_list[1].file_name, "file_name003")
        self.assertEqual(result_list[1].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[1].download_count, 0)
        self.assertEqual(result_list[1].comment, "comment003")

        self.assertEqual(result_list[2].report_id, "R000002")
        self.assertEqual(result_list[2].target_year, "2019")
        self.assertEqual(result_list[2].file_name, "file_name002")
        self.assertEqual(result_list[2].full_name, "first_name2 last_name2")
        self.assertEqual(result_list[2].download_count, 2)
        self.assertEqual(result_list[2].comment, "comment002")

        self.assertEqual(result_list[3].report_id, "R000001")
        self.assertEqual(result_list[3].target_year, "2019")
        self.assertEqual(result_list[3].file_name, "file_name001")
        self.assertEqual(result_list[3].full_name, "first_name1 last_name1")
        self.assertEqual(result_list[3].download_count, 2)
        self.assertEqual(result_list[3].comment, "comment001")
