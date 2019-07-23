from __future__ import print_function

import os.path
import pickle
import threading

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from config.settings.base import CREDENTIAL_ROOT, PROJECT_ROOT
from config.settings.develop import GOOGLE_TARGET_FOLDER_ID


class GoogleApiService:

    __scopes = ['https://www.googleapis.com/auth/drive']
    __mime_type = 'application/vnd.google-apps.document'

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(GoogleApiService, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def __get_service(self, scope):
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIAL_ROOT + 'credentials.json', scope)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)

        return service

    def create＿file(self, file_path, file_name):

        service = self.__get_service(self.__scopes)

        media_body = MediaFileUpload(
            PROJECT_ROOT + file_path,
            mimetype=self.__mime_type,
            resumable=True)

        body = {
            'name': file_name,
            'mimeType': self.__mime_type,
            'parents': [GOOGLE_TARGET_FOLDER_ID]
        }

        result = service.files().create(
            body=body,
            media_body=media_body
        ).execute()

        return result['id']

    def delete＿file(self, google_file_id):

        service = self.__get_service(self.__scopes)

        service.files().delete(
            fileId=google_file_id
        ).execute()

        return True

    def download＿file(self, google_file_id):

        service = self.__get_service(self.__scopes)

        file = service.files().export(
            fileId=google_file_id,
            mimeType="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ).execute()

        return file
