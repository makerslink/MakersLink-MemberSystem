from django.apps import AppConfig

# Based on https://github.com/CiCiUi/django-db-logger but modified to include app name

class MakerslinkLoggingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'makerslink_logging'
    verbose_name = 'Makerslink App Logs'
