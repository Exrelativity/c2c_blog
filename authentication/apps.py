from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    # Set the default primary key field type (AutoField is recommended)
    default_auto_field = "django.db.models.BigAutoField"  # You can keep this if it's necessary for your project
    name = "authentication"
