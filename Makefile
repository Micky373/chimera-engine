PYTHON := python

.PHONY: setup test spec-check

setup:
	@echo "Setup: install dependencies if needed"

test:
	@if command -v pytest >/dev/null 2>&1; then \
		pytest -q; \
	else \
		$(PYTHON) -m unittest discover -s tests -v; \
	fi

spec-check:
	@echo "Spec-check: placeholder (validate specs/ files)"

ci: setup test spec-check
	@echo "CI pipeline completed"

build-image:
	docker build -t chimera-ci .
