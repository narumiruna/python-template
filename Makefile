format:
	uv run ruff format .

lint:
	uv run ruff check .

type:
	uv run mypy --install-types --non-interactive .

test:
	uv run pytest -v -s --cov=src tests

publish:
	uv build -f wheel
	uv publish

all: format lint type test

.PHONY: lint test publish
