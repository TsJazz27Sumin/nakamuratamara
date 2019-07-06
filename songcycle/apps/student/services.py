# import area

def exist_email(email):
    return True

def exist_onetime_password(onetime_password):
    # TODO DBとの照合
    if(onetime_password is not None and onetime_password == "abc"):
        return True
    
    return False