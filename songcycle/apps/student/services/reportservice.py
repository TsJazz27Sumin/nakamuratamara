# import area
import threading

from apps.student.queries.applicationuserquery import ApplicationUserQuery
from apps.student.queries.numberingmasterquery import NumberingMasterQuery
from apps.student.services.googleapiservice import GoogleApiService
from apps.student.repositories.reportrepository import ReportRepository
from apps.student.queries.reportquery import ReportQuery
from apps.student.queries.downloadinformationquery import DownloadInformationQuery
from apps.student.repositories.downloadinformationrepository import DownloadInformationRepository


class ReportService:

    __singleton = None
    __applicationuserrquery = None
    __numberingmasterquery = None
    __googleapiservice = None
    __reportrepository = None
    __reportquery = None
    __downloadinformationrepository = None
    __downloadinformationquery = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(ReportService, cls).__new__(cls)
            cls.__applicationuserrquery = ApplicationUserQuery()
            cls.__numberingmasterquery = NumberingMasterQuery()
            cls.__googleapiservice = GoogleApiService()
            cls.__reportrepository = ReportRepository()
            cls.__reportquery = ReportQuery()
            cls.__downloadinformationrepository = DownloadInformationRepository()
            cls.__downloadinformationquery = DownloadInformationQuery()
        cls.__new_lock.release()
        return cls.__singleton

    def save_report(
            self,
            file_name,
            file_path,
            auther_user_id,
            target_year,
            comment,
            login_user_id):

        if(self.__applicationuserrquery.is_exist_user(auther_user_id) == False):
            json_data = {'data': {'message': 'Error'}}

        # Google Driveへのアップロード
        # https://developers.google.com/drive/api/v3/quickstart/python?hl=ja
        # 初回の認証は必要な様子。

        google_file_id = self.__googleapiservice.create＿file(
            file_path, file_name)
        report_id = self.__numberingmasterquery.get_report_id()

        self.__reportrepository.insert(
            report_id,
            auther_user_id,
            file_name,
            google_file_id,
            target_year,
            comment,
            login_user_id)

        return report_id

    def delete_report(self, report_id):

        report = self.__reportquery.get_one(report_id)

        if (report is None):
            return True

        self.__googleapiservice.delete＿file(report.google_file_id)
        self.__reportrepository.delete(report)

        download_informations = self.__downloadinformationquery.select_all_by_report_id(
            report_id)

        for download_information in download_informations:
            self.__downloadinformationrepository.delete(download_information)

        return True

    def download_report(self, report_id, user_id):

        report = self.__reportquery.get_one(report_id)

        if (report is None):
            return True

        file = self.__googleapiservice.download＿file(report.google_file_id)

        self.__downloadinformationrepository.insert(report_id, user_id)

        return file, report.file_name
