PYTHON := python

.PHONY: setup test spec-check

setup:
	@echo "Setup: install dependencies if needed"

test:
	$(PYTHON) -m unittest discover -v

spec-check:
	@echo "Spec-check: placeholder (validate specs/ files)"
