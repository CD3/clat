# justfile

# Default task to run when no command is specified
default: list

# List available tasks
list:
    @just --list

# Create the virtual environment
setup:
    @echo "Creating virtual environment..."
    @uv venv

# Install dependencies into the virtual environment
install:
    @echo "Installing dependencies..."
    @uv pip install -e ".[test,dev]"

# Run all tests
test: unit-tests cli-tests

# Run unit tests with pytest
unit-tests: install
    @echo "Running unit tests..."
    @uv run pytest -s tests/

# Run command-line interface tests with cram
cli-tests: install
    @echo "Running CLI tests..."
    @uv run cram tests/*.t

# Build the source distribution and wheel
build: install
    @echo "Building package..."
    @uv run python -m build

# Upload the package to PyPI
upload: build
    @echo "Uploading package..."
    @uv run twine upload dist/*

# Remove build artifacts and virtual environment
clean:
    @echo "Cleaning up..."
    @rm -rf .venv/ dist/ build/ clat.egg-info/ __pycache__/ .pytest_cache/
