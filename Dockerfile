# syntax=docker/dockerfile:1.4
ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}-slim as builder

    WORKDIR /app

    COPY requirements.txt .

    RUN python -m venv .venv
    ENV PATH="/app/.venv/bin:$PATH"

    RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt

FROM python:${PYTHON_VERSION}-alpine

    WORKDIR /app
    ENV PATH="/app/.venv/bin:$PATH"

    COPY --from=builder --link /app/.venv .venv

    COPY ebot ebot

    CMD [ "python", "-m", "ebot" ]
