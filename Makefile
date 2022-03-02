# Export application env vars (.prod | .test)
include deploy/.env.test
export

PROJECT_NAME := file-storage 
PROJECT_SRC := app

IMAGE_NAME := $(PROJECT_NAME)
APP_CONTAINER_NAME := $(PROJECT_SRC)

DOCKER := env docker
PYTHON := env python3
COMPOSE := env docker-compose


run:
	$(COMPOSE) up -d

build:
	$(COMPOSE) build

stop:
	$(COMPOSE) stop

down:
	$(COMPOSE) down

config:
	cat deploy/.env.prod

lint:
	$(PYTHON) -m flake8 $(PROJECT_SRC)

cs:
	$(PYTHON) -m black $(PROJECT_SRC) --target-version py310

test:
	$(PYTHON) -m pytest -vv

test-cov:
	$(PYTHON) -m pytest -vv --cov=$(PROJECT_SRC)

test-cov-html: test-cov
	$(PYTHON) -m coverage html
	$(PYTHON) -m webbrowser htmlcov/index.html

req:
	pip install -r requirements.txt
	pip install -r requirements.dev.txt
