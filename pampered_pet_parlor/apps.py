from django.apps import AppConfig


class PamperedPetParlorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pampered_pet_parlor'

class PamperedPetParlorConfig(AppConfig):
    name = 'pampered_pet_parlor'

    def ready(self):
        import pampered_pet_parlor.signals  # Import signals