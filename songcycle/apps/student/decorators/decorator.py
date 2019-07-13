import logging

from django.shortcuts import redirect
from user_agents import parse

from apps.student.queries.masterquery import MasterQuery

logger = logging.getLogger("student")

def no_authenticate(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            __output_ordinary_log(args, function_name)
            
            return function(*args, **kwargs)
        return wrapper
    return __decorator


def authenticate(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            __output_ordinary_log(args, function_name)

            if 'authority' not in args[0].session:
                # 権限が不明な場合は、セッション切れ、もしくは不正アクセスと見なし、強制ログアウト
                return redirect('request_login')
            return function(*args, **kwargs)

        return wrapper
    return __decorator

def authenticate_async(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            __output_ordinary_log(args, function_name)

            if 'authority' not in args[0].session:
                # 権限が不明な場合は、セッション切れ、もしくは不正アクセスと見なし、強制ログアウト
                return redirect('request_login')

            if (args[0].is_ajax() == False):
                # Ajax通信ではない場合、HOME画面に戻す。
                return redirect('home')

            return function(*args, **kwargs)

        return wrapper
    return __decorator

def authenticate_admin_only(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            __output_ordinary_log(args, function_name)

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

def authenticate_admin_only_async(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            __output_ordinary_log(args, function_name)

            if 'authority' not in args[0].session:
                # 権限が不明な場合は、セッション切れ、もしくは不正アクセスと見なし、強制ログアウト
                return redirect('request_login')
            else:
                if (args[0].is_ajax() == False):
                    # Ajax通信ではない場合、HOME画面に戻す。
                    return redirect('home') 

                if(args[0].session['authority'] == "admin"):
                    return function(*args, **kwargs)     
            
            # 管理者じゃない場合は、Home画面に戻す。
            return redirect('home')
        return wrapper
    return __decorator


def __output_ordinary_log(args, function_name):
        request = getattr(args[0], 'request', args[0])
        user_agent = parse(request.META['HTTP_USER_AGENT'])
        remote_addr = request.META['REMOTE_ADDR']

        user_id = ""
        if 'user_id' in request.session:
            user_id = request.session['user_id']

        logger.info('{} : {} : {} : {}'.format(user_agent, remote_addr, function_name, user_id))
