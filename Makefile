.PHONY: dev migrate seed seed-nosql docker-up docker-down help

help:
	@echo "Available commands:"
	@echo "  make dev          - Run the REST API development server"
	@echo "  make migrate      - Run SQL migrations"
	@echo "  make seed         - Run SQL seeders"
	@echo "  make seed-nosql   - Run NoSQL seeders"
	@echo "  make docker-up    - Start Docker services"
	@echo "  make docker-down  - Stop Docker services"

dev:
	uv run python src/apps/rest_api/main.py

migrate:
	uv run python src/core/database/sql/migrate.py

seed:
	uv run python src/core/database/sql/seeder.py

seed-nosql:
	uv run python src/core/database/nosql/seeder.py

docker-up:
	docker compose up -d --wait

docker-down:
	docker compose down
