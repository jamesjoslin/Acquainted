from django.apps import AppConfig

#registers application
class UserAuthentificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
