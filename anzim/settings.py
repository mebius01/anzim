import os
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

SECRET_KEY = config('SECRET_KEY')
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=False, cast=int)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=False, cast=bool)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False, cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=False, cast=bool)
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=False, cast=bool)
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)
X_FRAME_OPTIONS = os.environ.get('X_FRAME_OPTIONS', default='SAMEORIGIN')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'blog',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'taggit',
    'taggit_serializer',
    'debug_toolbar',
    'ckeditor',
    'corsheaders',
]

CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST', cast=Csv())

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'anzim.urls'

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
                'blog.context_processors.title_list.title_list',
                'blog.context_processors.title_list.tag_list',
            ],
        },
    },
]

WSGI_APPLICATION = 'anzim.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config("DB_ENGINE"),
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': config("DB_HOST"),
        'PORT': config("DB_PORT", cast=int),
    }
}

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
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH =  os.path.join(BASE_DIR, 'uploads')
STATIC_ROOT = config('STATIC_ROOT')
MEDIA_ROOT = config('MEDIA_ROOT')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

INTERNAL_IPS = '127.0.0.1'

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
# Определяет срок действия писем с подтверждением по электронной почте
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=3
# Пользователь обязан передать адрес электронной почты при регистрации.
ACCOUNT_EMAIL_REQUIRED = True
# Определяет метод проверки электронной почты при регистрации ("mandatory" "optional" "none")
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# Предел попыток входа в систему
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
# Период времени в секундах от последней неудачной попытки
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT= 400
# URL (или имя URL), к которому нужно вернуться после выхода пользователя из системы
ACCOUNT_LOGOUT_REDIRECT_URL = '/'


#EMAIL
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True)

# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    # https://vivazzi.pro/it/ckeditor-config/
    'default': {
        'toolbar': [
            [
            '-', 'Source',
            '-', 'Undo', 'Redo',
            '-', 'Bold', 'Italic', 'Underline',
            '-', 'Link', 'Unlink', 'Anchor',
            '-', 'Format', 'FontSize',
            '-', 'Maximize',
            '-', 'Table',
            '-', 'Image',
            '-', 'NumberedList', 'BulletedList'
            ],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
            '-', 'TextColor',
            '-', 'Outdent', 'Indent',
            '-', 'HorizontalRule',
            '-', 'Blockquote'
            ],
            ['CodeSnippet', ],
        ],
        'extraPlugins': 'codesnippet',
        'codeSnippet_languages': {
            'bash': 'Bash',
            'python': 'Python',
            'javascript': 'JavaScript',
            'html': 'HTML',
            'json': 'Json',
            'css': 'CSS',
            'scss': 'Scss',
            'less': 'Less',
            'apache': 'Apache',
            'nginx': 'Nginx',
            'http': 'HTTP',
            'SQL' : 'SQL',
            'makefile': 'Makefile',
            'shell': 'Shell Session',
        },
        'codeSnippet_theme': 'monokai',
        'disableNativeSpellChecker': False,
        'removePlugins': 'liststyle, tabletools, scayt, menubutton, contextmenu',
        'language': 'ru',
        'height': 500,
        'width': '100%',
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True,
    }
}