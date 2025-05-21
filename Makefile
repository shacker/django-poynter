all: dev_refresh

PYTHON_VERSION=$(cat .python-version)

.venv/bin/python$(PYTHON_VERSION):
	uv venv --prompt $(shell basename $(shell pwd)) .venv

requirements.txt: pyproject.toml
	uv pip compile --generate-hashes $< -o $@ $(REQ_ARGS)

requirements.dev.txt: pyproject.toml requirements.txt
	uv pip compile --generate-hashes $< --extra dev --constraints requirements.txt -o $@ $(REQ_ARGS)

.PHONY: install
install: .venv/bin/python$(PYTHON_VERSION)
	uv pip install -r requirements.dev.txt
	uv pip install -e .

.PHONY: dev_refresh
dev_refresh: install
	.venv/bin/manage.py migrate
	.venv/bin/pre-commit install
