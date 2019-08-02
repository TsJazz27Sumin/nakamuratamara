from django.test import TestCase

from apps.student.repositories.reportrepository import ReportRepository
from apps.student.queries.reportquery import ReportQuery


class ReportRepositoryTestCase(TestCase):

    def test(self):

        report_id = "R000001"
        auther_user_id = "U0001"
        file_name = "file_name001"
        google_file_id = "g0001"
        target_year = "2019"
        comment = "comment001"
        login_user_id = "U0000"

        ReportRepository().insert(report_id,
                                  auther_user_id,
                                  file_name,
                                  google_file_id,
                                  target_year,
                                  comment,
                                  login_user_id)
        
        report = ReportQuery().get_one(report_id)

        self.assertEqual(report.auther_user_id, "U0001")
        self.assertEqual(report.file_name, "file_name001")
        self.assertEqual(report.google_file_id, "g0001")
        self.assertEqual(report.target_year, "2019")
        self.assertEqual(report.comment, "comment001")
        self.assertEqual(report.create_user_id, "U0000")
        self.assertEqual(report.update_user_id, "U0000")

        ReportRepository().delete(report)

        report = ReportQuery().get_one(report_id)
        self.assertEqual(report, None)
