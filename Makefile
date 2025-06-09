tests:
	pytest tests/unit_test

format:
	isort .
	black .

lint:
	pylint src/*.py