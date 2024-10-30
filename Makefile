install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest test.py
	py.test --nbval *.ipynb

format:
	black *.ipynb &&\
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns= *.py
	
all: install lint test format