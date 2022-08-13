## The Makefile includes instructions on environment setup and lint tests
# Create and activate a virtual environment
# Install dependencies in requirements.txt
# Dockerfile should pass hadolint
# app.py should pass pylint and flake8

setup:
	python3 -m venv ~/.venv-capstone

install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

lint:
	hadolint Dockerfile
	pylint app.py --disable=C0111,C0114,C0116
	flake8 app.py

all: setup install lint