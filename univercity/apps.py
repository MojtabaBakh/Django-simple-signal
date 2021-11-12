from django.apps import AppConfig


class UnivercityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'univercity'
    
    def ready(self) :
        import univercity.signals
