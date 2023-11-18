from django.apps import AppConfig


class CounterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.counter'
    verbose_name = 'Счетчик запросов'
