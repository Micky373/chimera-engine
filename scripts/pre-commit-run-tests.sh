#!/usr/bin/env bash
set -euo pipefail

echo "Running pre-commit tests..."
make test
echo "Pre-commit tests passed."
