# Better call Saul 🔎

[![Build Status](https://travis-ci.org/anapaulagomes/saul.svg?branch=master)](https://travis-ci.org/anapaulagomes/saul) [![Code Climate](https://codeclimate.com/github/anapaulagomes/saul/badges/gpa.svg)](https://codeclimate.com/github/anapaulagomes/saul) [![Code Health](https://landscape.io/github/anapaulagomes/saul/master/landscape.svg?style=flat)](https://landscape.io/github/anapaulagomes/saul/master)

Saul is a tool to analyze git logs and suggest areas of improvement, based on the project history.

## Local Development

### Setting up virtualenv

```
pyenv virtualenvwrapper
mkvirtualenv saul-dev
pip install -r requirements.txt
```

### Running tests

```
pytest tests
tox # runs on python 2.7, 3.4, 3.5 and 3.6
```

### Running Saul

```
export PYTHONPATH=.
python saul/main.py # will read saul.log
```

### Generating log file

```
git log --raw --no-merges > saul.log
```
