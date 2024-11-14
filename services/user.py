from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from db.models import User


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None) -> User:

    user = get_user_model().objects.create_user(
        username=username,
        password=password
    )

    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name

    user.save()
    return user


def get_user(user_id: int) -> User:
    try:
        return get_user_model().objects.get(id=user_id)
    except ObjectDoesNotExist:
        raise ValueError(f"User with ID '{user_id}' does not exist.")


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> User:

    try:
        user = get_user_model().objects.get(id=user_id)
    except ObjectDoesNotExist:
        raise ValueError(f"User with ID '{user_id}' does not exist.")

    if username:
        user.username = username
    if password:
        user.set_password(password)
    if last_name:
        user.last_name = last_name
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name

    user.save()
    return user