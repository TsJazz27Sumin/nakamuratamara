# import area

# CRUDのCUDは、ここに集約する。

def save_access_information(access_information):
    access_information.save()

def save_temporarily_login_url(temporarily_login_url):
    temporarily_login_url.save()

def save_application_user(application_user):
    application_user.save()