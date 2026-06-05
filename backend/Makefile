run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

fix:
	ruff check . --fix

check:
	ruff check .
	ruff format . --check
	pytest