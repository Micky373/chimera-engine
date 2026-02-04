FROM python:3.12-slim
WORKDIR /app
COPY . /app
# Install runtime deps in CI or locally as needed
CMD ["python", "-m", "unittest", "discover", "-v"]
