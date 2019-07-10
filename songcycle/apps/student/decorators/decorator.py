from django.shortcuts import redirect
from apps.student.queries.masterquery import MasterQuery
import logging
from user_agents import parse

logger = logging.getLogger("student")

def no_authenticate(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            request = getattr(args[0], 'request', args[0])
            user_agent = parse(request.META['HTTP_USER_AGENT'])
            remote_addr = request.META['REMOTE_ADDR']

            logger.info('{} : {} : {}'.format(user_agent, remote_addr, function_name))
            
            return function(*args, **kwargs)
        return wrapper
    return __decorator


def authenticate(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            request = getattr(args[0], 'request', args[0])
            user_agent = parse(request.META['HTTP_USER_AGENT'])
            remote_addr = request.META['REMOTE_ADDR']

            logger.info('{} : {} : {}'.format(user_agent, remote_addr, function_name))

            if 'authority' not in args[0].session:
                # 権限が不明な場合は、セッション切れ、もしくは不正アクセスと見なし、強制ログアウト
                return redirect('request_login')
            return function(*args, **kwargs)
        return wrapper
    return __decorator

def authenticate_admin_only(function_name):
    def __decorator(function):
        def wrapper(*args, **kwargs):

            request = getattr(args[0], 'request', args[0])
            user_agent = parse(request.META['HTTP_USER_AGENT'])
            remote_addr = request.META['REMOTE_ADDR']

            logger.info('{} : {} : {}'.format(user_agent, remote_addr, function_name))

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
