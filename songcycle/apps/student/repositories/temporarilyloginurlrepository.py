# import area
from student.models.temporarilyloginurl import TemporarilyLoginUrl

# CRUDのCUDは、ここに集約する。

def insert(request_email, onetime_password):
    
    temporarily_login_url = TemporarilyLoginUrl(
        request_email = request_email,
        onetime_password = onetime_password
    )

    temporarily_login_url.save()
