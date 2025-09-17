# Python Practice

[![CI](https://github.com/<TU_USUARIO>/python-practice/actions/workflows/python-ci.yml/badge.svg)](https://github.com/<TU_USUARIO>/python-practice/actions/workflows/python-ci.yml)
[![codecov](https://codecov.io/gh/<TU_USUARIO>/python-practice/branch/main/graph/badge.svg)](https://codecov.io/gh/<TU_USUARIO>/python-practice)

This repository contains Python exercises and mini-projects to practice and improve coding skills.

## Code Quality and Automation

This project follows strict code quality and formatting standards to ensure maintainability and readability.

### Tools Used

- **Black** – An opinionated code formatter that automatically formats code to follow PEP8 standards.  
  Usage:  
  ```bash
  black .
- **Isort** – Automatically sorts and organizes imports alphabetically and by groups.
  Usage:
  ```bash
  isort .

- **Flake8** – Linter that checks for code style issues, unused variables, and potential errors.
  Usage:
  ```bash
  flake8 .
- **mypy** – Static type checker to validate Python type hints.
  Usage:
  ```bash
  mypy .
- **pre-commit** – Runs all formatting and linting checks automatically before each commit.
  Setup:
  ```bash
  pre-commit install
- **Bandit** – Security analyzer that detects common security issues in Python code.
  Usage:
  ```bash
  bandit -r .
These tools together help maintain a consistent code style, reduce bugs, and enforce best practices across the project.