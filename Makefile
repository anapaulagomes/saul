help:
	@echo "clean - remove Python file artifacts"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "install - install saul dependencies"
	@echo "setup - install saul dependencies and development dependencies"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"

clean:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +

coverage:
	@pytest --cov=saul tests/ --cov-branch

install:
	  @pip install -r requirements.txt

lint:
	@flake8 .

setup:
	@$(MAKE) install
	@pip install -r requirements-dev.txt

test:
	@pytest tests

test-all:
	@tox -r
