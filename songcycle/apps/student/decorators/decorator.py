from django.shortcuts import redirect
from student.queries.masterquery import MasterQuery

def authenticate(function):
    def wrapper(*args, **kwargs):
        if 'authority' not in args[0].session:
            # 権限が不明な場合は、セッション切れ、もしくは不正アクセスと見なし、強制ログアウト
            return redirect('request_login')
        return function(*args, **kwargs)
    return wrapper

def authenticate_admin_only(function):
    def wrapper(*args, **kwargs):
        if 'authority' not in args[0].session:
            # 権限が不明な場合は、セッション切れ、もしくは不正アクセスと見なし、強制ログアウト
            return redirect('request_login')
        else:
            if(args[0].session['authority'] == "admin"):
                return function(*args, **kwargs)        
        
        # 管理者じゃない場合は、Home画面に戻す。
        return redirect('home')
    return wrapper
