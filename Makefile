# Variabler
PYTHON := python3
PIP := pip3
PYTHONPATH := $(shell pwd)
export PYTHONPATH

# Installera beroenden
install:
	@echo "Installing dependencies...\n"
	$(PIP) install -r requirements.txt

# Kör programmet
run:
	@echo "Running the program...\n"
	$(PYTHON) code/py/login_window.py

# Rensa upp
clean:
	@echo "Cleaning up...\n"
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .pytest_cache

# Generera dokumentation med pyreverse
.PHONY: uml

uml:
	@echo "Generating UML diagrams with pyreverse...\n"
	mkdir -p doc
	find code/py -name "*.py" | xargs pyreverse -o png -p smartshop
	mv classes_smartshop.png doc/classes.png
	mv packages_smartshop.png doc/packages.png

.PHONY: pdoc

pdoc:
	@echo "Generating HTML documentation with pdoc...\n"
	$(PYTHON) -m pdoc -o doc code/py
	@echo "Documentation generated in doc/pydoc/ directory."
