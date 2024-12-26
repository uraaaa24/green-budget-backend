# PostgreSQL
DB_CONTAINER_NAME = green-budget-db
DB_USER = postgres
DB_NAME = postgres

.PHONY: build up down logs db-connect clean

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

db-connect:
	docker exec -it ${DB_CONTAINER_NAME} psql -U ${DB_USER} -d ${DB_NAME}

clean:
	docker compose down --rmi all --volumes --remove-orphans
