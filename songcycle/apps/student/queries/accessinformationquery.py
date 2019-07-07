# import area
from student.models.accessinformation import AccessInformation

# CRUDのRは、ここに集約する。

def get_fault_count(remote_addr, target_date):
    return AccessInformation.objects.filter(remote_addr=remote_addr, access_date=target_date, fault_value__isnull=False).count()