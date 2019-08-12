"""
Django settings for songcycle project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

#pycache
sys.dont_write_bytecode = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5adur&m%2033fsw91q0^g+-&chy6g-t6$1l%ns%r0u)&*e4y1n'

# SECURITY WARNING: don't run with debug turned on in production!
# ローカルで404.htmlや500.htmlを出したい場合は以下設定。
# DEBUG = False
# ALLOWED_HOSTS = ['127.0.0.1']
DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup', #レコードの削除・更新時にファイルも削除する。
    'bootstrap4',
    'compressor', 
    'static_precompiler',
    'student'
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (                                                                                                                                     
    ('text/es6+javascript', 'babel -o {outfile} {infile}'),                                                                                                   
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':[ 
                'bootstrap4.templatetags.bootstrap4',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_TZ = True

USE_I18N = True

USE_L10N = True


# Fetch Django's project directory
DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Fetch the project_root
PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)

# Add apps/ to the Python path
sys.path.append(os.path.join(PROJECT_ROOT, "apps"))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = (
    os.path.join(PROJECT_ROOT, 'media')
)

CREDENTIAL_ROOT = (
    os.path.join(PROJECT_ROOT, 'config/credential/')
)

# セッションの設定
SESSION_COOKIE_AGE = 3600 # 60分
SESSION_SAVE_EVERY_REQUEST = True # 1リクエストごとにセッション情報を更新

# ログ設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # TODO:デフォルトの設定はDEBUGフラグで開発・本番の切り替えを行っているが、そもそも別のファイルにするのが主流かつ安全。
    #　herokuにデプロイ後、例外ログ含めちゃんと出るか確認。
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s a',
        },
        'verbose': {
            'format': '【%(levelname)s 】%(asctime)s : %(module)s : %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            #'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler', 
            'formatter': 'verbose'
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        #TODO:ファイル出力
        'student': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# develop.py and production.py are inclueded APIKEY. So I don't commit and push to GitHub.
# If you want to run application. The followings are settings in develop.py. I hope you can refer to it.
# And there is command.txt under /support directory. I listed command for install requirement.
# Also there is master data within master.sql in same directory.

# develop.py production.pyについては、APIKEYも含まれるのでGitHubにCommitしていません。
# もしローカル環境で動かしたい場合は、以下が「develop.py」で設定している項目なので、参考にしていただければと思います。
# また、/support配下に「command.txt」があります。こちらにinstallが必要と思われるコマンドは並べてあります。
# マスタデータについても「master.sql」を同じ階層に配置しています。

# from .base import *
# import os


# # Database 
# # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         # https://stackoverflow.com/questions/39767810/cant-install-psycopg2-package-through-pip-install-is-this-because-of-sierra
#         'NAME': 'songcycle',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': '127.0.0.1',
#         'POST': '5432',
#         'TEST': {
#             'NAME': 'test_songcycle',
#         }
#     }
# }

# ローカルで動かす分には、sendgridは設定しなくてもいいかと思います。
# コンソールにログインURLを出力する状態でcommitしてあります。

# SENDGRID_APIKEY = "YOUR SENDGRID_APIKEY"
# SENDGRID_FROM = "YOUR SENDGRID_FROM"

# ファイルアップロード機能を試したい場合は、こちらを設定いただくと同時に、DriveAPIが使えるように設定いただければと思います。
# GOOGLE_TARGET_FOLDER_ID = 'YOUR GOOGLE_TARGET_FOLDER_ID'
# REPORT_SUMMARY_PASSWORD = 'sample'
