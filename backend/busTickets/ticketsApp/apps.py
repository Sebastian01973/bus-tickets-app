from django.apps import AppConfig


class TicketsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ticketsApp'

    def ready(self):
        from ticketsApp.signals.signals import log_user_logged_in_failed, log_user_logged_in_success
