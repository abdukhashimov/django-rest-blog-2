from django.apps import AppConfig
from user.signals import password_reset_token_created


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        return password_reset_token_created
