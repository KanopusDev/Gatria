# Installation Guide

## Table of Contents

- [System Requirements](#system-requirements)
- [Recommended Setup](#recommended-setup)
  - [Creating a Virtual Environment](#creating-a-virtual-environment)
- [Basic Installation](#basic-installation)
- [Optional Feature Installations](#optional-feature-installations)
  - [Web Framework Support](#web-framework-support)
  - [Database Integrations](#database-integrations)
  - [Asynchronous Support](#asynchronous-support)
  - [Machine Learning Features](#machine-learning-features)
- [Post-Installation Steps](#post-installation-steps)
- [Troubleshooting](#troubleshooting)

---

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.8 or higher
- **Package Manager**: `pip` (comes with Python)
- **Internet Access**: Required for installing packages

---

## Recommended Setup

### Creating a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

---

## Basic Installation

Install Gatria using `pip`:

```bash
pip install Gatria
```

Verify the installation:

```bash
pip show Gatria
```

---

## Optional Feature Installations

Enhance Gatria by installing optional packages according to your needs.

### Web Framework Support

Install support for web frameworks:

```bash
pip install Gatria[web]
```

### Database Integrations

Install database support:

```bash
pip install Gatria[database]
```

### Asynchronous Support

Enable asynchronous functionalities:

```bash
pip install Gatria[async]
```

### Machine Learning Features

Install machine learning libraries:

```bash
pip install Gatria[ml]
```

---

## Post-Installation Steps

After installing Gatria and optional packages:

1. **Set up configurations**: Refer to the [Configuration Guide](./configuration.md) to set up database connections and environment variables.
2. **Initialize the database**: Run database migrations if necessary.
3. **Test the installation**: Run a sample script to ensure everything is working.

---

## Troubleshooting

### Common Issues

- **Module Not Found**: Ensure that the virtual environment is activated and packages are installed.
- **Version Conflicts**: Check for conflicting package versions with `pip list` and resolve by updating or downgrading as needed.
- **Permission Errors**: Run installations with appropriate permissions or use a virtual environment to avoid system-wide changes.

For further assistance, please refer to the [FAQ](./faq.md) or contact the support team.