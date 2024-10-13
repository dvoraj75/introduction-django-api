from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "introduction_api.apps.user"
    label = "user"
    verbose_name = "User"
