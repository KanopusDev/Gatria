# Contributing to Gatria

We are excited to have you contribute to the Gatria project! Your contributions help improve the project and are greatly appreciated.

---

## Table of Contents

- [Development Environment Setup](#development-environment-setup)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Code of Conduct](#code-of-conduct)

---

## Development Environment Setup

1. **Fork** the repository to your GitHub account.
2. **Clone** your forked repository:

   ```bash
   git clone https://github.com/your-username/Gatria.git
   ```

3. **Navigate** to the project directory:

   ```bash
   cd Gatria
   ```

4. **Create** a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

5. **Install** development dependencies:

   ```bash
   pip install -e .[dev]
   ```

6. **Install** optional dependencies as needed:

   ```bash
   pip install -e .[all]
   ```

---

## Development Workflow

- **Create a branch** for your changes:

  ```bash
  git checkout -b feature/your-feature-name
  ```

- **Make commits** to your branch as you progress.

- **Ensure** your code is up to date with the main branch:

  ```bash
  git fetch origin
  git rebase origin/main
  ```

- **Run tests** and ensure all tests pass before submitting:

  ```bash
  pytest
  ```

---

## Coding Standards

Maintain code quality by adhering to the following standards:

- **PEP 8**: Follow Python's PEP 8 style guide for code formatting.
- **Type Annotations**: Use type hints where applicable.
- **Docstrings**: Write clear and concise docstrings for modules, classes, and methods.
- **Comments**: Comment complex logic and algorithms.

### Code Formatting Tools

- **Black**: Code formatter.
  ```bash
  black .
  ```

- **isort**: Sorts imports.
  ```bash
  isort .
  ```

- **Flake8**: Style guide enforcement.
  ```bash
  flake8
  ```

- **Mypy**: Static type checker.
  ```bash
  mypy .
  ```

---

## Commit Message Guidelines

- **Format**: Use the imperative mood in subject lines.
- **Structure**:

  ```
  Short summary (50 characters or less)

  More detailed description, if necessary. Wrap the body at 72 characters.
  ```

- **References**: Reference issues and pull requests when applicable.

---

## Pull Request Process

1. **Push** your branch to GitHub:

   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create** a pull request from your branch to `main`:

   - Provide a clear and descriptive title.
   - Include a detailed description of changes.

3. **Participate** in the code review:

   - Respond to feedback.
   - Make necessary changes.
   - Update your PR accordingly.

4. **Approval**:

   - Once approved by maintainers, your PR will be merged.

---

## Issue Reporting

If you encounter bugs or have feature requests:

- **Search** existing issues to avoid duplicates.
- **Open** a new issue with a descriptive title and detailed information.
- **Provide** steps to reproduce, if reporting a bug.

---

## Code of Conduct

We are committed to fostering an open and welcoming environment. All participants are expected to adhere to our Code of Conduct:

- **Be Respectful**: Treat everyone with respect and consideration.
- **Collaborate**: Be open to ideas and feedback.
- **Communicate**: Use clear and concise language.
- **Inclusivity**: Encourage diverse perspectives.

For more details, refer to our [Code of Conduct](./CODE_OF_CONDUCT.md).

---

Thank you for contributing to Gatria!