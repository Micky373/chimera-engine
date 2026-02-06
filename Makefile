PYTHON := python

.PHONY: setup test spec-check

setup:
	@echo "Setup: install dependencies if needed"

test:
	$(PYTHON) -m unittest discover -s tests -v

spec-check:
	@echo "Spec-check: placeholder (validate specs/ files)"

ci: setup test spec-check
	@echo "CI pipeline completed"

build-image:
	docker build -t chimera-ci .
