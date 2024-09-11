format-source:
	python -m black src/
	python -m isort src/

format-tests:
	python -m black tests/
	python -m isort tests/

lint-source:
	-python -m flake8 src/
	-python -m mypy src/

lint-tests:
	-python -m flake8 tests/
	-python -m mypy tests/

test:
	python -m pytest tests

all: format-source format-tests lint-source lint-tests test
