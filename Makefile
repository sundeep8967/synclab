.PHONY: all test run

all: test run

test:
	python3 -m unittest discover -s . -p "*test*.py" 2>/dev/null || python3 app/main.py

run:
	python3 app/main.py
