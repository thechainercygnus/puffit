# Development Workflow Overview

This document outlines the development workflow managed by three GitHub Actions: `publish.yml`, `test.yml`, and `version.yml`. These workflows automate testing, badge updates, version bumping, and package publishing to PyPI, providing a streamlined CI/CD process.

## 1. Test and Update Badges (`test.yml`)

### Trigger:
- Runs on every push to any branch (`push` event for `**`).

### Steps:
1. **Checkout the repository**:
   - Uses `actions/checkout@v4` to pull the current branch into the workflow environment.
   
2. **Set up Python**:
   - Sets up Python 3.12.5 using `actions/setup-python@v4`.
   
3. **Install testing dependencies**:
   - Installs the required packages for testing, including `pytest`, `pytest-cov`, and `coverage-badge`.
   
4. **Run tests and generate coverage report**:
   - Executes all tests using `pytest`, collects test coverage with `pytest-cov`, and generates an XML report for the results.
   
5. **Generate a coverage badge**:
   - Creates a badge (`coverage.svg`) representing the current test coverage using `coverage-badge`.
   
6. **Update `README.md` with the coverage badge**:
   - Uses `sed` to update the `README.md` file with the latest coverage badge.
   - Commits these changes to the branch with the commit message "Update coverage badge."
   
7. **Push changes to the branch**:
   - Pushes the updated `README.md` and coverage badge back to the current branch using the repository's `ACTIONS_PAT` token for authentication.

## 2. Version Bump (`version.yml`)

### Trigger:
- Automatically triggered when a pull request to the `main` branch is closed (`pull_request` event).
- Can also be manually triggered (`workflow_dispatch` event).

### Steps:
1. **Checkout the repository**:
   - Uses `actions/checkout@v4` to retrieve the current `main` branch.

2. **Set up Python**:
   - Sets up Python 3.12.5 using `actions/setup-python@v4`.

3. **Install dependencies**:
   - Installs dependencies defined in the `requirements.txt` file.

4. **Determine version bump type**:
   - Detects labels applied to the pull request (e.g., `major`, `minor`, `patch`).
   - Defaults to `patch` if no specific label is found.
   
5. **Bump version**:
   - Executes `bump2version` with the determined bump type (major/minor/patch) using Poetry.

6. **Push version bump**:
   - Pushes the updated version and tags to the `main` branch.

## 3. Publish to PyPI (`publish.yml`)

### Trigger:
- Runs on every push of a tag matching `v*` (e.g., `v1.0.0`).

### Steps:
1. **Checkout the repository**:
   - Uses `actions/checkout@v4` to pull the current state of the repository.

2. **Set up Python**:
   - Sets up Python 3.12.5 using `actions/setup-python@v4`.

3. **Install Poetry**:
   - Installs Poetry using the official installation script.
   - Configures Poetry to avoid using virtual environments (`virtualenvs.create false`).

4. **Install dependencies**:
   - Exports production dependencies (`--without=dev`) to `requirements_build.txt`.
   - Installs these dependencies along with `twine`.

5. **Build the package**:
   - Uses `python -m build` to build the package into the `dist/` folder.

6. **Publish to PyPI**:
   - Publishes the built package to PyPI using `twine`, authenticating with the repository's `PYPI_TOKEN` secret.

## Summary

- **Testing**: Every push runs tests and updates the coverage badge.
- **Versioning**: When a PR is merged to `main`, the version is bumped automatically based on labels and pushed to the repository.
- **Publishing**: When a new version tag is pushed, the package is built and published to PyPI.

This process ensures continuous testing, consistent versioning, and smooth releases to PyPI.
