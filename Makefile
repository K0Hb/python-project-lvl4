runserver:
	python3 manage.py runserver

lint:
	@poetry run flake8

selfcheck:
	@poetry check

check: selfcheck lint

build: check
	@poetry build

test:
	@poetry run coverage run manage.py test
	@poetry run coverage xml

install:
	@poetry install

translate:
	poetry run python manage.py makemessages -l ru

compilemessages:
	poetry run python manage.py compilemessages

migrate:
	python3 manage.py migrate