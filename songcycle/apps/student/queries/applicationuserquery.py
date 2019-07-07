# import area
from student.models.applicationuser import ApplicationUser
from student.functions import function
from student.services import masterservice

# CRUDのRは、ここに集約する。
def is_active_user(email):
    return ApplicationUser.objects.filter(email=email, active=masterservice.get_active_user_status()).count() == 1

def get_active_user(email):
    return ApplicationUser.objects.filter(email=email, active=masterservice.get_active_user_status()).first()
