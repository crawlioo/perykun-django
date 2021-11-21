# heroku staging settings
run-staging-env:
	heroku config:set DJANGO_SETTINGS_MODULE=core.settings.staging \
	&& heroku config:set SECRET_KEY='django-insecure-@azm=_jp7!!-$q5@liti-qy4-o4!je(v&o_moahssqu_&-jsc8'

run-dev:
	python manage.py runserver