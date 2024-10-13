from django.contrib.auth.models import AbstractUser

from introduction_api.common.models import BaseModel


class User(BaseModel, AbstractUser):
    class Meta:
        ordering = ["pk"]
        db_table = "user"
