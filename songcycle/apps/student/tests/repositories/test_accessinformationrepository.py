from django.test import TestCase

from apps.student.repositories.accessinformationrepository import AccessInformationRepository
from apps.student.queries.accessinformationquery import AccessInformationQuery


class AccessInformationRepositoryTestCase(TestCase):

    def test(self):

        event_type = "event_type"
        http_accept_language = "http_accept_language"
        browser = "browser"
        browser_version = "browser_version"
        os = "os"
        os_version = "os_version"
        device = "device"
        device_brand = "device_brand"
        device_type = "device_type"
        remote_addr = "remote_addr"
        success_value = "success_value"
        fault_value = "fault_value"
        comment = "comment"

        AccessInformationRepository().insert(
            event_type,
            http_accept_language,
            browser,
            browser_version,
            os,
            os_version,
            device,
            device_brand,
            device_type,
            remote_addr,
            success_value,
            fault_value,
            comment
        )

        result_list = AccessInformationQuery().select_all()
        result = result_list[0]

        self.assertEqual(result.event_type, event_type)
        self.assertEqual(result.http_accept_language, http_accept_language)
        self.assertEqual(result.browser, browser)
        self.assertEqual(result.browser_version, browser_version)
        self.assertEqual(result.os, os)
        self.assertEqual(result.os_version, os_version)
        self.assertEqual(result.device, device)
        self.assertEqual(result.device_brand, device_brand)
        self.assertEqual(result.device_type, device_type)
        self.assertEqual(result.remote_addr, remote_addr)
        self.assertEqual(result.success_value, success_value)
        self.assertEqual(result.fault_value, fault_value)
        self.assertEqual(result.comment, comment)
