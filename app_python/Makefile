init:
	pip3 install pre-commit
	apt install python3-venv
	python3 -m venv venv
	@echo "Run 'source venv/bin/activate' to run venv"
	@echo "Run 'pip install -r requirements.txt' to install packages"

run:
	PYTHONPATH=. python3 src/web/__main__.py

test:
	PYTHONPATH=. pytest tests -v

lint:
	flake8 src

typecheck:
	pyright
