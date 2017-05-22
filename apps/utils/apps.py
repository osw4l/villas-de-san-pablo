from django.apps import AppConfig

from apps.utils.print_colors import _red


class UtilsConfig(AppConfig):
    name = 'apps.utils'
    verbose_name = 'utils'

    def ready(self):
        print(_red('Ready Utils'))
