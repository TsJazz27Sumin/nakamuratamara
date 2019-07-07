# import area
from student.models.applicationuser import ApplicationUser
from student import functions

# CRUDのRは、ここに集約する。
def is_active_user(email):
    return ApplicationUser.objects.filter(email=email, active=functions.get_active_user_status()).count() == 1

def get_active_user(email):
    return ApplicationUser.objects.filter(email=email, active=functions.get_active_user_status()).first()
