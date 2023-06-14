"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from django.conf import settings as django_settings
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

BASE_URL = 'http://localhost:8000'

APP_NAME = 'Blog'

EMAIL = 'exrelativity@gmail.com'
# please  dont use because is not mine
G_MAP_API_KEY = 'YOUR_API_KEY'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)u+uirxemo2cc@!0cpaxz+_ui&$do++nbc3-+63#_@xlhy2tm)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'daphne',
    "channels",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles", # Required for GraphiQL
    "django_jsonfield_backport",
    'graphene_django',
    'graphql_auth',
    'django_filters',
    "blog",
    "post",
    "userprofile",
    "authentication",
    "file",
    "debug_toolbar",
]
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "blog.middleware.current_user_middleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "blog.urls"
TEMPLATE_DIR = BASE_DIR/'template'
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
                "django.template.context_processors.media",
            ],
        },
    },
]

SETTINGS_EXPORT = [
    'BASE_DIR',
    'BASE_URL',
    'APP_NAME',
    'EMAIL',
    'G_MAP_API_KEY',
]

WSGI_APPLICATION = "blog.wsgi.application"
ASGI_APPLICATION = "blog.asgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
   "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "tutorial_blog",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        'ATOMIC_MUTATIONS': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


MEDIA_ROOT = "media-assets/"

MEDIA_URL = "media-assets/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# STATIC_ROOT = "static"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

ASSETS_ROOT = BASE_DIR/STATIC_URL


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "authentication.Users"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_VERIFICATION = "none"

GRAPHENE = {
    'SCHEMA': 'blog.schema.schema',
    'SCHEMA_OUTPUT': 'schema.json',
    'SCHEMA_INDENT': 4,
    'MIDDLEWARE': (
        'blog.middleware.AuthorizationMiddleware',
        'blog.middleware.AuthenticationMiddleware',
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ),
    'RELAY_CONNECTION_ENFORCE_FIRST_OR_LAST': False,
    'RELAY_CONNECTION_MAX_LIMIT': 300,
    'ATOMIC_MUTATIONS': True,
    'CAMELCASE_ERRORS': True,
    'SUBSCRIPTION_PATH': '/ws/graphql',
    'GRAPHIQL_HEADER_EDITOR_ENABLED': True,
}

AUTHENTICATION_BACKENDS = [
    # 'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
    "graphql_auth.backends.GraphQLAuthBackend",

]

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,

    # optional
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True, 
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
        
    ],
}


# DEFAULTS = {
#     # if allow to login without verification,
#     # the register mutation will return a token
#     "ALLOW_LOGIN_NOT_VERIFIED": True,
#     # mutations fields options
#     "LOGIN_ALLOWED_FIELDS": ["email", "username"],
#     "ALLOW_LOGIN_WITH_SECONDARY_EMAIL": True,
#     # required fields on register, plus password1 and password2,
#     # can be a dict like UPDATE_MUTATION_FIELDS setting
#     "REGISTER_MUTATION_FIELDS": ["email", "username"],
#     "REGISTER_MUTATION_FIELDS_OPTIONAL": [],
#     # optional fields on update account, can be list of fields
#     "UPDATE_MUTATION_FIELDS": {"first_name": "String", "last_name": "String"},
#     # tokens
#     "EXPIRATION_ACTIVATION_TOKEN": timedelta(days=7),
#     "EXPIRATION_PASSWORD_RESET_TOKEN": timedelta(hours=1),
#     "EXPIRATION_SECONDARY_EMAIL_ACTIVATION_TOKEN": timedelta(hours=1),
#     "EXPIRATION_PASSWORD_SET_TOKEN": timedelta(hours=1),
#     # email stuff
#     "EMAIL_FROM": getattr(django_settings, "DEFAULT_FROM_EMAIL", "exrelativity@gmail.com"),
#     "SEND_ACTIVATION_EMAIL": True,
#     # client: example.com/activate/token
#     "ACTIVATION_PATH_ON_EMAIL": "activate",
#     "ACTIVATION_SECONDARY_EMAIL_PATH_ON_EMAIL": "activate",
#     # client: example.com/password-set/token
#     "PASSWORD_SET_PATH_ON_EMAIL": "password-set",
#     # client: example.com/password-reset/token
#     "PASSWORD_RESET_PATH_ON_EMAIL": "password-reset",
#     # email subjects templates
#     "EMAIL_SUBJECT_ACTIVATION": "email/activation_subject.txt",
#     "EMAIL_SUBJECT_ACTIVATION_RESEND": "email/activation_subject.txt",
#     "EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION": "email/activation_subject.txt",
#     "EMAIL_SUBJECT_PASSWORD_SET": "email/password_set_subject.txt",
#     "EMAIL_SUBJECT_PASSWORD_RESET": "email/password_reset_subject.txt",
#     # email templates
#     "EMAIL_TEMPLATE_ACTIVATION": "email/activation_email.html",
#     "EMAIL_TEMPLATE_ACTIVATION_RESEND": "email/activation_email.html",
#     "EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION": "email/activation_email.html",
#     "EMAIL_TEMPLATE_PASSWORD_SET": "email/password_set_email.html",
#     "EMAIL_TEMPLATE_PASSWORD_RESET": "email/password_reset_email.html",
#     "EMAIL_TEMPLATE_VARIABLES": {},
#     # query stuff
#     "USER_NODE_EXCLUDE_FIELDS": ["password", "is_superuser"],
#     "USER_NODE_FILTER_FIELDS": {
#         "email": ["exact"],
#         "username": ["exact", "icontains", "istartswith"],
#         "is_active": ["exact"],
#         "status__archived": ["exact"],
#         "status__verified": ["exact"],
#         "status__secondary_email": ["exact"],
#     },
#     # turn is_active to False instead
#     "ALLOW_DELETE_ACCOUNT": False,
#     # string path for email function wrapper, see the testproject example
#     "EMAIL_ASYNC_TASK": False,
#     # mutation error type
#     "CUSTOM_ERROR_TYPE": None,
#     # registration with no password
#     "ALLOW_PASSWORDLESS_REGISTRATION": False,
#     "SEND_PASSWORD_SET_EMAIL": False,
# }