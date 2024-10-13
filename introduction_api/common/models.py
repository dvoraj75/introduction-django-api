from typing import Any

from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.db import models

from introduction_api.common.enums import ApiErrorCode


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def update(self, **data: dict[str, Any]) -> None:
        for field_name, value in data.items():
            try:
                if (field := self._meta.get_field(field_name)).is_relation and not isinstance(field, models.ForeignKey):
                    getattr(self, field_name).set(value)
                else:
                    setattr(self, field_name, value)
            except FieldDoesNotExist as e:
                raise ValidationError(
                    f"Field {field_name} does not exist",
                    params={"field": "field_name", "value": value},
                    code=ApiErrorCode.FIELD_DOES_NOT_EXIST,
                ) from e
