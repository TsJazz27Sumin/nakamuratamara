from django.shortcuts import redirect

def authenticate(function):
    def wrapper(*args, **kwargs):
        if 'authority' not in args[0].session:
            # 権限が不明な場合は、強制ログアウト
            return redirect('request_login')
        return function(*args, **kwargs)
    return wrapper
