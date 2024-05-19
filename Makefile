install:
	poetry install

lint:
	ruff check .

type:
	mypy --install-types --non-interactive .

test:
	pytest -v -s --cov=. tests

cover:
	pytest -v -s --cov=. --cov-report=xml tests

publish:
	poetry build -f wheel
	poetry publish

.PHONY: lint test publish
