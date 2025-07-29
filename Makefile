.PHONY: start stop build restart shell migrate createsuperuser logs

start:
	docker-compose up --build

stop:
	docker-compose down

build:
	docker-compose build

restart:
	docker-compose down
	docker-compose up --build

shell:
	docker-compose exec web sh

migrate:
	docker-compose exec web python manage.py migrate

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

logs:
	docker-compose logs -f web