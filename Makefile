start:
	COMPOSE_HTTP_TIMEOUT=200 docker-compose up


migrate:
	docker-compose run --rm api python manage.py makemigrations\
	&& docker-compose run --rm api python manage.py migrate \
	&& docker container stop nu-db


superuser:
	docker-compose run --rm api python manage.py createsuperuser \
	&& docker container stop nu-db


seed:
	docker-compose run --rm api python manage.py flush \
	&& docker-compose run --rm api python manage.py loaddata seed \
	&& docker container stop nu-db


connectdb:
	docker-compose run db psql -U postgres postgres -h 172.18.0.2


update:
	docker-compose run --rm api python manage.py makemigrations\
	&& docker-compose run --rm api python manage.py migrate \
	&& docker-compose run --rm api python manage.py loaddata seed \
	&& docker container stop nu-db
