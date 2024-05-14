# Variabler
PYTHON := python3
PIP := pip3

# Installera beroenden
install:
	$(PIP) install -r requirements.txt

# Kör programmet
run:
	$(PYTHON) code/py/login_window.py

# Rensa upp
clean:
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .pytest_cache

# Generera dokumentation med pyreverse
pyreverse:
	@echo "Generating UML diagrams with pyreverse..."
	mkdir -p doc/pyreverse
	find code/py -name "*.py" | xargs pyreverse -o png -p project_name
	pyreverse code /*.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot
