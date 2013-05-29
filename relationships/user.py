"""Module to support both Django 1.5 custom user class and classic ones.

It only defines User which is an alias to:
 * the result of get_user_model() in Django 1.5
 * django.contrib.auth.models.User in previous versions
"""
try:
    from django.contrib.auth import get_user_model
except ImportError:  # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()
