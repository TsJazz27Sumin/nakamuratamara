from django.test import TestCase

from apps.student.queries.downloadinformationquery import DownloadInformationQuery
from apps.student.models.downloadinformation import DownloadInformation


class DownloadInformationQueryTestCase(TestCase):

    def setUp(self):
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

    def test_select_all_by_report_id_case1(self):

        result_list = DownloadInformationQuery().select_all_by_report_id('R000001')
        self.assertEqual(len(result_list), 2)

        self.assertEqual(result_list[0].report_id, "R000001")
        self.assertEqual(result_list[0].user_id, "U0001")

        self.assertEqual(result_list[1].report_id, "R000001")
        self.assertEqual(result_list[1].user_id, "U0002")

    def test_get_count_dictionary_case1(self):

        result = DownloadInformationQuery().get_count_dictionary([
            'R000001', 'R000002'])
        self.assertEqual(result['R000001'], '2')
        self.assertEqual(result['R000002'], '2')
