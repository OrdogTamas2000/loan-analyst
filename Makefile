.PHONY: up down test test-int lint ingest process ask eval api

# Targets beyond test/lint start working as their tasks land (compose in A.1, CLI in A.5+).

up:
	docker compose up -d

down:
	docker compose down

test:
	uv run pytest -m "not integration"

test-int:
	uv run pytest -m integration

lint:
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy src

ingest:
	uv run loan-analyst ingest

process:
	uv run loan-analyst process

ask:
	uv run loan-analyst ask "$(Q)"

eval:
	uv run loan-analyst eval

api:
	uv run uvicorn loan_analyst.api.main:app --reload
