import os
from pathlib import Path
from datetime import timedelta
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# Application settings
BASE_URL = 'http://localhost:8000'
APP_NAME = 'Blog'
EMAIL = 'exrelativity@gmail.com'
G_MAP_API_KEY = 'YOUR_API_KEY'

# Debug and security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-)u+uirxemo2cc@!0cpaxz+_ui&$do++nbc3-+63#_@xlhy2tm)')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['yourdomain.com', 'your-ip-address']

# Installed apps
INSTALLED_APPS = [
    'daphne',
    "channels",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
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
INTERNAL_IPS = ["127.0.0.1"]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "blog.middleware.current_user_middleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Template settings
TEMPLATE_DIR = BASE_DIR / 'template'
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

# Database settings
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "tutorial_blog",
#         "USER": "root",
#         "PASSWORD": "",
#         "HOST": "127.0.0.1",
#         "PORT": "3306",
#         'ATOMIC_MUTATIONS': True,
#     }
# }


SECRET_KEY = config("SECRET_KEY")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "ATOMIC_MUTATIONS": True,
    }
}

# Password validation
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

# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = '/media-assets/'
MEDIA_ROOT = BASE_DIR / 'media-assets/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
ASSETS_ROOT = BASE_DIR / STATIC_URL

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth user model
AUTH_USER_MODEL = "authentication.Users"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server.com'
EMAIL_PORT = 587  # Adjust to your SMTP server's port
EMAIL_USE_TLS = True  # Use TLS or SSL based on your server's requirements
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

# GraphQL settings
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

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    "graphql_auth.backends.GraphQLAuthBackend",
]

# GraphQL JWT settings
GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
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
