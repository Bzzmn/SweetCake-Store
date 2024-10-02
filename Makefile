install: 
	#install commands
	python -m pip install --upgrade pip &&\
	python -m pip install -r requirements.txt
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
	docker build -t sweetcake .

run-local:
	#run check if container exists and if so remove it then run container
	@if [ $$(docker ps -a -q -f name=sweetcake) ]; then \
	docker rm -f sweetcake; \
	fi
	docker run --env-file .env --name sweetcake -p127.0.0.1:8000:8000 sweetcake

all: install format lint test build run