# import area
from student.models.temporarilyloginurl import TemporarilyLoginUrl

# CRUDのRは、ここに集約する。

def is_valid_onetime_password(onetime_password, valid_timestamp):
    return TemporarilyLoginUrl.objects.filter(onetime_password=onetime_password, send_email_date_timestamp__gt=valid_timestamp).first()