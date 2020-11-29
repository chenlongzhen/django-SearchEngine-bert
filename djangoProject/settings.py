"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xl-fih!_a%$c9vgv6)phy86akb0c+lh+159-(3xul7isp-@z#$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'app01.apps.App01Config',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'templates'/ 'search']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# mysql 配置 demo
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'bookmanager',
#         'HOST': '127.0.0.1',
#         'PORT': 3306,
#         'USER': 'root',
#         'PASSWORD': '123456',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
#  路径 https://blog.csdn.net/xujin0/article/details/83421626
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 配置 全文检索框架(haystack)使用 检索引擎(whoosh)
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        # haystack 通过 下面路径 中的 WhooshEngine类，来使用whoosh检索引擎
        # WhooshEngine的路径 venv/lib/site-packages/haystack/backends/whoosh_backend.py WhooshEngine类
        #'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine', #英文有结果
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        #'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        # 索引文件的 存放路径，所有的 索引文件 都存放在 该目录下。生成索引文件时，自动 在目录(BASE_DIR)下 创建目录(whoosh_index)
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

# 检索引擎(whoosh)的作用: 对 表中的某些字段 进行 关键词分析，在 关键词 和 表中其它记录s 之间 建立联系(索引表)
# 表中 字段内容 发生变化时，索引 也应发生变化 来适应 字段内容的变化。

# 当表中数据 发生变化(添加 删除 修改)时，自动生成 新的索引(替换 旧的索引)
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'