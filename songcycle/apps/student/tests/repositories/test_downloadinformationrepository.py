from django.test import TestCase
from datetime import datetime, timedelta
from django.utils.crypto import get_random_string

from apps.student.repositories.downloadinformationrepository import DownloadInformationRepository
from apps.student.queries.downloadinformationquery import DownloadInformationQuery


class DownloadInformationRepositoryTestCase(TestCase):

    def test(self):

        report_id = "R000001"
        user_id = "U0001"

        DownloadInformationRepository().insert(report_id, user_id)

        result_list = DownloadInformationQuery().select_all_by_report_id(report_id)
        download_information = result_list[0]

        self.assertEqual(download_information.report_id, report_id)
        self.assertEqual(download_information.user_id, user_id)

        DownloadInformationRepository().delete(download_information)

        result_list = DownloadInformationQuery().select_all_by_report_id(report_id)

        self.assertEqual(len(result_list), 0)
