from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        import your_app_name.signals  # Replace 'your_app_name' with the name of your app


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
