install:
	$(PYTHON) -m pip install -r requirements.txt

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"
installed:
	$(PYTHON) -m pip list
	@printf "installed"
lint:
	flake8 .
	pylint .

docs:
	pdoc --html code --output-dir docs

test:
	coverage run -m pytest
	coverage report -m

robot-test:
	robot code.robot

.PHONY: install lint docs sphinx test robot-test
