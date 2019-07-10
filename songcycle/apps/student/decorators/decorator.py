from django.shortcuts import redirect
from apps.student.queries.masterquery import MasterQuery
import logging

def no_authenticate(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):
            print("no_authenticate : " + function_name)
            return function(*args, **kwargs)
        return wrapper
    return __decorator


def authenticate(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):
            
            print("authenticate : " + function_name)

            if 'authority' not in args[0].session:
                # 権限が不明な場合は、セッション切れ、もしくは不正アクセスと見なし、強制ログアウト
                return redirect('request_login')
            return function(*args, **kwargs)
        return wrapper
    return __decorator

def authenticate_admin_only(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            print("authenticate_admin_only : " + function_name)

            if 'authority' not in args[0].session:
                # 権限が不明な場合は、セッション切れ、もしくは不正アクセスと見なし、強制ログアウト
                return redirect('request_login')
            else:
                if(args[0].session['authority'] == "admin"):
                    return function(*args, **kwargs)        
            
            # 管理者じゃない場合は、Home画面に戻す。
            return redirect('home')
        return wrapper
    return __decorator
