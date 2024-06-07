# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: setup.py
	python3 -m pip install --upgrade pip
	python3 -m pip install virtualenv
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -e .

# venv is a shortcut target
venv: $(VENV)/bin/activate

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv clean