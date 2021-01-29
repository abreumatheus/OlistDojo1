from typing import Type


def validate_type(value: object, type: Type, key: str):
    if not isinstance(value, type):
        raise TypeError(f"{key.capitalize()} must be {type}.")
    return value


def validate_not_empty(value: str, key: str):
    if not value.strip():
        raise ValueError(f"{key.capitalize()} can't be empty.")
    return value


def validate_len(value: object, max_len: int, key: str):
    if len(value) > max_len:
        raise ValueError(f"{key.capitalize()} can't be greater than {max_len} characters.")
    return value
