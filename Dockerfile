FROM kestra/kestra:latest

USER root

# Copy filenest-python-sdk to the exact relative path expected by pyproject.toml (../filenest-python-sdk relative to /app/aipipeline)
COPY filenest-python-sdk /app/filenest-python-sdk
COPY aipipeline/pyproject.toml aipipeline/uv.lock aipipeline/README.md /app/aipipeline/

# Install filenest, email-validator, and all dependencies into Kestra's environment using uv
RUN uv pip install --python /app/.venv /app/filenest-python-sdk \
    && uv pip install --python /app/.venv "pydantic[email]" \
    && uv pip install --python /app/.venv -r /app/aipipeline/pyproject.toml
