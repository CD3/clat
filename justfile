# justfile

# Default virtual environment directory
VENV_DIR := ".venv"

# Path to uv executable in the virtual environment
UV := "{{VENV_DIR}}/bin/uv"
# Path to python executable in the virtual environment
PYTHON := "{{VENV_DIR}}/bin/python"

# Default task to run when no command is specified
default: test

# Create the virtual environment and install dependencies
install:
    # Create virtual environment if it doesn't exist
    @if [ ! -d "{{VENV_DIR}}" ]; then \
        echo "Creating virtual environment in {{VENV_DIR}}..."; \
        uv venv {{VENV_DIR}}; \
    fi
    # Install dependencies
    @echo "Installing dependencies..."
    @{{UV}} pip install -e ".[test,dev]"

# Run all tests
test: unit-tests cli-tests

# Run unit tests with pytest
unit-tests: install
    @echo "Running unit tests..."
    @{{PYTHON}} -m pytest -s tests/

# Run command-line interface tests with cram
cli-tests: install
    @echo "Running CLI tests..."
    @{{PYTHON}} -m cram tests/*.t

# Build the source distribution and wheel
build: install
    @echo "Building package..."
    @{{PYTHON}} -m build

# Upload the package to PyPI
upload: build
    @echo "Uploading package..."
    @{{PYTHON}} -m twine upload dist/*

# Remove build artifacts and virtual environment
clean:
    @echo "Cleaning up..."
    @rm -rf {{VENV_DIR}} dist/ build/ clat.egg-info/ __pycache__/ .pytest_cache/
