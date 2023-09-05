.PHONY: lint
lint:
	flake8 *.py

.PHONY: format
format:
	black *.py
	isort *.py

.PHONY: run
run:
	uvicorn main:app --reload