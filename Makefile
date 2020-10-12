.PHONY: default lint test

default: lint test

lint:
	autopep8 -i *.py
	flake8 *.py

test:
	python -m unittest
