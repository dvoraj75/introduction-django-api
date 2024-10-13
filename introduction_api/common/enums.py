from enum import StrEnum


class ApiErrorCode(StrEnum):
    # lookup errors
    FIELD_DOES_NOT_EXIST = "field_does_not_exist"
