make migrateprod:
	DJANGO_SETTINGS_MODULE=backstage.settings.production ./manage.py migrate

make migrate:
	DJANGO_SETINGS_MODULE=backstage.settings.local ./manage.py makemigrations
	DJANGO_SETTINGS_MODULE=backstage.settings.local ./manage.py migrate
start:
	DJANGO_SETTINGS_MODULE=backstage.settings.local ./manage.py runserver_plus

shell:
	DJANGO_SETTINGS_MODULE=backstage.settings.local ./manage.py shell_plus
