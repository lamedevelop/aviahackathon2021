PROJECT_NAME ?= aviahackaton2021
VERSION = $(shell python3 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= Oleggr
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make lint	- Check code with flake8"
	@echo "make test	- Run tests"
	@exit 0

lint:
	flake8 app --count --exit-zero --exclude=app/db/migrations/ --max-complexity=10 --max-line-length=127 --statistics
	flake8 tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test:
	pytest -s

docker-run:
	docker build -t ar_server:latest .
	docker run --rm -it -p 4000:4000 -d ar_server:latest
