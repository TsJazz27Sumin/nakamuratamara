# import area
from student.models import AccessInformation, ApplicationUser
from . import functions

# CRUDのRは、ここに集約する。

def get_fault_count(remote_addr, target_date):
    return AccessInformation.objects.filter(remote_addr=remote_addr, access_date=target_date, fault_value__isnull=False).count()

def is_active_user(email):
    return ApplicationUser.objects.filter(email=email, active=functions.get_active_user_status()).count() == 1