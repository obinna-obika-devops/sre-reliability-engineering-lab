PYTHON ?= python3

.PHONY: install test run lint
install:
	$(PYTHON) -m pip install -r app/requirements.txt

test:
	$(PYTHON) -m pytest app/tests -q

run:
	$(PYTHON) -m uvicorn app.main:app --host 0.0.0.0 --port 8000

lint:
	$(PYTHON) -m compileall app
