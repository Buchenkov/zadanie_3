"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.1.NN

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-82ab0rp+q!0_t0^vkkvt&xoyo4)2htg2@bewl*=c0302icxomc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # для - DEBUG = False
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'modeltranslation',   # обязательно впишите его перед админом

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'news.apps.NewsConfig',
    'django_filters',
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',  # отвечает за выход через Yandex
    'subscriptions',
    'django_apscheduler',
    # 'rest_framework',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Пожалуй, один из главных промежуточных слоев, потому что он реализует различные проверки безопасности — XSS, nosniff, HSTS, CORS, поддержка SSL и т. д.
    'django.contrib.sessions.middleware.SessionMiddleware',  # Включает механизм сессий в разрабатываемом приложении.
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',  # для пакета gettext
    # Рекомендуемый для использования во всех Django-проектах, потому что он позволяет выполнять стандартные процедуры над URL
    'django.middleware.csrf.CsrfViewMiddleware',  # Включает проверку безопасности от угроз типа CSRF.
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Реализует основы аутентификации и идентификации.
    'django.contrib.messages.middleware.MessageMiddleware',
    # Включает поддержку сообщений, лежащих в основе работы с куки и сессиями.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # обеспечивают простую в использовании защиту от кликджекинга
    'allauth.account.middleware.AccountMiddleware',
    'news.middlewares.TimezoneMiddleware',   # add that middleware!
]

# SOCIALACCOUNT_PROVIDERS = {   # ещё вариант, не через админку
#     'yandex': {
#         'APP': {
#             'client_id': '0944d864ef4a4c80b932844064159f4d',
#             'secret': '80331f60205c4cf1b7f1d5e7e5e5ccca',
#             'key': ''
#         }
#     }
# }

ROOT_URLCONF = 'project.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # os.path.join(BASE_DIR, 'templates')
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

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'NewsPaper',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True  # интернационализация

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static', ]

# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5    # Ограничение попыток входа в систему
LOGIN_URL = '/account/login/'
# LOGOUT_REDIRECT_URL = '/account/login/'
LOGIN_REDIRECT_URL = "/"

# Первые два параметра указывают на то, что поле email является обязательным и уникальным. Третий, наоборот, — говорит,
# что username необязательный. Следующий параметр указывает, что аутентификация будет происходить посредством
# электронной почты. Напоследок мы указываем, что верификация почты отсутствует.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # 'none'
# mandatory — не пускать пользователя на сайт до момента подтверждения почты;
# optional — сообщение о подтверждении почты будет отправлено, но пользователь может залогиниться на сайте без подтверждения почты.
ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignupForm'}
ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # позволит избежать дополнительного входа и активирует аккаунт сразу,
# как только мы перейдём по ссылке.
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7  # хранит количество дней, когда доступна ссылка на подтверждение регистрации

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # который просто напечатает его в консоли.
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "igorchan"
EMAIL_HOST_PASSWORD = "jwitospiqdwbrxpf"
# EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = ['NewsPortal']
DEFAULT_FROM_EMAIL = "igorchan@yandex.ru"

# # ++++ вариант из вебинара
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_USE_SSL = True
# DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')


SERVER_EMAIL = "igorchan@yandex.ru"
MANAGERS = [
    ('igor', 'igorchan@mail.ru'),
]

ADMINS = (
    ('igor', 'igorchan@yandex.ru'),  # текст в account/forms.py
)

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25
SITE_URL = 'http://127.0.0.1:8000'

# ### Celery
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'  # 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# * CELERY_BROKER_URL — указывает на URL брокера сообщений (Redis). По умолчанию он находится на порту 6379.
# * CELERY_RESULT_BACKEND — указывает на хранилище результатов выполнения задач.
# * CELERY_ACCEPT_CONTENT — допустимый формат данных.
# * CELERY_TASK_SERIALIZER — метод сериализации задач.
# * CELERY_RESULT_SERIALIZER — метод сериализации результатов.

# Кэширование
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': os.path.join(BASE_DIR, 'cache_files'),  # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
#         # 'TIMEOUT': 60,
#     }
# }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # средства форматирования
    'formatters': {
        'format_debug': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },

        'format_warning_mail': {
            'format': '{asctime} {levelname} {message} {pathname} ',
            'style': '{',
        },

        'format_general_security_info': {
            'format': '{asctime} {levelname} {message} {module} ',
            'style': '{',
        },

        'format_error_critical': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },
    },
    # обработчики
    'handlers': {
        'console_debug': {
            'level': 'INFO',   # 'DEBUG'
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_debug',
        },

        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_warning_mail',
        },

        'console_gen_sec_info': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'format_general_security_info',
            'filename': 'general.log',
        },

        'console_error_critical': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_error_critical',
        },

        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'format_error_critical',
            'filename': 'errors.log',
        },

        'security_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'format_general_security_info',
            'filename': 'security.log',
        },

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'format_warning_mail',
        },
    },
    # фильтры
    'filters': {
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
    },
    # регистраторы
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_gen_sec_info', 'console_error_critical'],
            'level': 'INFO',   # 'DEBUG'
            'propagate': True,
        },

        'django.request': {
            # Этот логгер обрабатывает все сообщения вызванные HTTP-запросами и вызывает исключения для определенных кодов состояния. Все коды ошибок HTTP 5xx будут вызывать сообщения об ERROR. Аналогичным образом, коды HTTP 4xx будут отображаться в виде WARNING
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.server': {
            # Когда сервер запускается с помощью команды runserver, он будет регистрировать сообщения, связанные с обработкой этих запросов
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.db.backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.security': {
            'handlers': ['security_file'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

# LOGGING = {
#     'version': 1,   # единственный вариант
#     'disable_existing_logger': False,   # джанговский логгер
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'news'],    # ['console', 'news'],  # большой вывод в консоль
#             'level': 'DEBUG',
#         },
#     },
#     'handlers': {   # обработка
#         'console': {    # вывод в консоль
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'myformatter',
#         },
#         'news': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',  # как обрабатывается - в файл
#             'filename': 'debug.log',
#             'formatter': 'myformatter',
#             # 'filters': ['require_debug_false'],
#         },
#     },
#     'formatters': {
#         'myformatter': {
#             'format': '{levelname} {message} {asctime}',
#             'datetime': '%Y.%m.%d. %H:%M:%S',
#             'style': '{',
#         },
#     },
#     'filters': {    # Далее определен фильтр, который пропускает записи только в случае, когда DEBUG = True.
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',   # обрабатывать если debug - false
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',    # обрабатывать если debug - True
#         },
#     },
# }

#
# TEST_LOGGER_NAME = 'test_logger'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#
#     'formatters': {
#         'full': {
#             'format': '[{module} {asctime} {levelname}] {message}',
#             'style': '{',
#         },
#     },
#
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'full',
#         },
#     },
#
#     'loggers': {
#         TEST_LOGGER_NAME: {
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#     }
# }
#
# test_logger = logging.getLogger(TEST_LOGGER_NAME)
