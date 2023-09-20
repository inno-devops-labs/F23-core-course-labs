"""App module"""
from django.apps import AppConfig

class MyappConfig(AppConfig):
    """My App configuration"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
