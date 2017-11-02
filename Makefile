help:
	@echo "clean - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

lint:
	@flake8 .

test:
	@pytest tests

test-all:
	@tox -r

coverage:
	@pytest --cov=saul tests/ --cov-branch

