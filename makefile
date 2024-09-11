format:
	poetry run black src/
	poetry run isort src/

lint:
	-poetry run flake8 src/
	-poetry run mypy src/

test:
	poetry run pytest

all: format lint
