from django.apps import AppConfig


class LinksConfig(AppConfig):
	default_auto_field = "django.db.models.BigAutoField"
	name = "links"
	verbose_name = 'Сокращение ссылок'

	def ready(self):
		import links.signals
