PYTHON := python

.PHONY: setup test spec-check

setup:
	@echo "Setup: install dependencies if needed"

install-hooks:
	@if command -v pre-commit >/dev/null 2>&1; then \
		pre-commit install; \
		pre-commit install -t pre-push; \
		echo "pre-commit hooks installed"; \
	else \
		echo "pre-commit not installed; run 'pip install pre-commit'"; \
	fi

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
