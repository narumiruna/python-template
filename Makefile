install:
	poetry install

lint:
	poetry run ruff check .

type:
	poetry run mypy --install-types --non-interactive .

test:
	poetry run pytest -v -s --cov=. tests

cover:
	poetry run pytest -v -s --cov=. --cov-report=xml tests

publish:
	poetry build -f wheel
	poetry publish

.PHONY: lint test publish
