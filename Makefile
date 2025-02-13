install: 
	#install commands
	pip install hatch &&\
	uv pip install -r pyproject.toml &&\
	pip install pylint pylint-django

format: 
	#format code
	python -m black *.py webPages/*.py sweetcake/*.py

lint:
	#flake8 or #pylint
	python -m pylint --load-plugins pylint_django --django-settings-module=sweetcake.settings --disable=R,C,W1203 *.py webPages/*.py sweetcake/*.py --ignore=migrations

test:
	#test
	python -m pytest -vv --cov=webPages

build:
	#build container
	docker build \
		--build-arg DJANGO_SECRET_KEY="$${DJANGO_SECRET_KEY}" \
		--build-arg DATABASE_URL="$${DATABASE_URL}" \
		-t sweetcake .

run-local:
	#run check if container exists and if so remove it then run container
	@if [ $$(docker ps -a -q -f name=sweetcake) ]; then \
	docker rm -f sweetcake; \
	fi
	docker run --env-file .env --name sweetcake -p 127.0.0.1:8000:8000 sweetcake

clean:
	# Stop and remove containers
	@if [ $$(docker ps -a -q -f name=sweetcake) ]; then \
		docker rm -f sweetcake; \
	fi
	# Remove images
	@if [ $$(docker images -q sweetcake) ]; then \
		docker rmi -f sweetcake; \
	fi
	# Remove unused images and cache
	docker system prune -f

all: install format lint test build run