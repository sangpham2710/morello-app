test:
	docker-compose run --rm app sh -c "python manage.py wait_for_database && python manage.py test"

testapp:
	docker-compose run --rm app sh -c "python manage.py wait_for_database && python manage.py test $(app)"

lint:
	docker-compose run --rm app sh -c "flake8"

check:
	make test && make lint

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

startapp:
	docker-compose run --rm app sh -c "python manage.py startapp $(name)"

makemigrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm app sh -c "python manage.py migrate"

shell:
	docker-compose run --rm app sh -c "python manage.py shell"

clean:
	docker-compose down -v

createsuperuser:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"

populate:
	docker-compose run --rm app sh -c "python manage.py populate_database"