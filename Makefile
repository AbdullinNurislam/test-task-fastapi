init:
	cp -u .env.sample .env

R=docker compose

up:
	$R up -d

db:
	$R up -d app_db

alembic:
	$R run --rm alembic

alembic-current:
	$R run --rm --entrypoint="bash -c 'cd src && alembic current'" alembic

app:
	$R up -d app --force-recreate

down:
	$R down

build:
	$R build

build-no-cache:
	$R build --no-cache

logs:
	$R logs --tail 100 -f app

# test:
# 	$R 
