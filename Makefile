export DB_USER := admin
export DB_PASSWORD := admin
export DB_PORT := 5432
export DB_NAME := testing
export LOCALHOST := localhost

LOCAL_DB_CONN := postgresql+psycopg2://$(DB_USER):$(DB_PASSWORD)@$(LOCALHOST):$(DB_PORT)/$(DB_NAME)

it: test

build: build/install-dependencies

build/install-dependencies:
	pip install -r requirements.txt

test: build dependencies/start test/run dependencies/clean

test/run:
	pytest

dependencies/start: dependencies/database/run dependencies/database/migrate

dependencies/clean: dependencies/database/stop

dependencies/database/run:
	docker-compose up -d
	sleep 10

dependencies/database/migrate:
	alembic -x DB_URL=$(LOCAL_DB_CONN) upgrade head

dependencies/database/stop:
	docker-compose stop && docker-compose rm -vf

deploy/migrate-db:
	alembic -x DB_URL="postgresql+psycopg2://$(DB_USER):$(DB_PASSWORD)@$(LOCALHOST):$(DB_PORT)/$(DB_NAME)" upgrade head