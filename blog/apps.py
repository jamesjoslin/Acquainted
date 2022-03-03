from django.apps import AppConfig

#how my app is understood. need to understand more of this

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
