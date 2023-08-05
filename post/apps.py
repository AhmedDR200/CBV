from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'



class SuitConfig(DjangoSuitConfig):
    layout = "vertical"