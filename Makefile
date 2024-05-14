# Variabler
PYTHON := python3
PIP := pip3

# Installera beroenden
install:
	$(PIP) install -r requirements.txt

# Kör test
test:
	$(PYTHON) -m unittest discover -s tests

# Kör programmet
run:
	$(PYTHON) src/main.py

# Rensa upp
clean:
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .pytest_cache
