# import area
from student.models.accessinformation import AccessInformation
from student.models.applicationuser import ApplicationUser
from student.models.temporarilyloginurl import TemporarilyLoginUrl
from . import functions

# CRUDのRは、ここに集約する。

def get_fault_count(remote_addr, target_date):
    return AccessInformation.objects.filter(remote_addr=remote_addr, access_date=target_date, fault_value__isnull=False).count()

def is_active_user(email):
    return ApplicationUser.objects.filter(email=email, active=functions.get_active_user_status()).count() == 1

def get_active_user(email):
    return ApplicationUser.objects.filter(email=email, active=functions.get_active_user_status()).first()

def is_valid_onetime_password(onetime_password, valid_timestamp):
    return TemporarilyLoginUrl.objects.filter(onetime_password=onetime_password, send_email_date_timestamp__gt=valid_timestamp).first()