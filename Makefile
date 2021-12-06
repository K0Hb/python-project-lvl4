runserver:
	python3 manage.py runserver

lint:
	@poetry run flake8

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build