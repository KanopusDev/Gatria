# API Reference

## Overview

This document provides a comprehensive reference of all classes, methods, and modules available in the Gatria employee management system.

---

## Core Modules

- [`Gatria.manager`](#Gatriammanagermodule): Core management classes.
- [`Gatria.models`](#Gatriammodelsmodule): Data models and schemas.
- [`Gatria.adapters`](#Gatriamadaptersmodule): Framework adapters.
- [`Gatria.database`](#Gatriamdatabasemodule): Database integrations.
- [`Gatria.ml`](#Gatriammlmodule): Machine Learning components.

---

## `Gatria.manager` Module

### `EmployeeManager` Class

The `EmployeeManager` class provides methods to manage employee records.

#### Initialization

```python
EmployeeManager(
    framework: str = 'flask',
    database: Union[str, DatabaseAdapter] = 'sql',
    async_mode: bool = False,
)
```

- **Parameters**:
  - `framework` (str): The web framework to integrate with. Options are `'flask'`, `'django'`, `'fastapi'`.
  - `database` (str or DatabaseAdapter): The database to use. Options are `'sql'`, `'mongodb'`, `'redis'`, or a custom database adapter instance.
  - `async_mode` (bool): Enables asynchronous operations when set to `True`.

#### Methods

- `create_employee(data: dict) -> Employee`
  - **Description**: Creates a new employee record.
  - **Parameters**:
    - `data` (dict): A dictionary containing employee details.
  - **Returns**: An `Employee` instance.
  - **Example**:
    ```python
    employee = manager.create_employee({
        "name": "Alice Brown",
        "position": "Project Manager",
        "department": "Operations",
    })
    ```

- `get_employee(id: str) -> Employee`
  - **Description**: Retrieves an employee by ID.
  - **Parameters**:
    - `id` (str): The unique identifier of the employee.
  - **Returns**: An `Employee` instance.
  - **Example**:
    ```python
    employee = manager.get_employee("emp456")
    ```

- `update_employee(id: str, data: dict) -> Employee`
  - **Description**: Updates an existing employee's data.
  - **Parameters**:
    - `id` (str): The unique identifier of the employee.
    - `data` (dict): A dictionary of fields to update.
  - **Returns**: The updated `Employee` instance.

- `delete_employee(id: str) -> bool`
  - **Description**: Deletes an employee record.
  - **Parameters**:
    - `id` (str): The unique identifier of the employee.
  - **Returns**: `True` if deletion was successful, `False` otherwise.

#### Asynchronous Methods

When `async_mode` is enabled, the following asynchronous methods are available:

- `async create_employee_async(data: dict) -> Employee`
- `async get_employee_async(id: str) -> Employee`
- `async update_employee_async(id: str, data: dict) -> Employee`
- `async delete_employee_async(id: str) -> bool`

---

## `Gatria.models` Module

### `Employee` Class

Represents an employee in the system.

#### Attributes

- `id` (str): Unique identifier.
- `name` (str): Full name.
- `position` (str): Job title.
- `department` (str): Department name.
- `email` (str): Email address.
- `phone` (str): Phone number.
- `date_hired` (datetime): Date of hiring.

#### Methods

- `to_dict() -> dict`
  - Converts the employee object to a dictionary.
- `from_dict(data: dict) -> Employee`
  - Creates an `Employee` instance from a dictionary.

---

## `Gatria.adapters` Module

Framework adapters allow integration with various web frameworks.

### Flask Adapter

```python
from Gatria.adapters.flask import FlaskAdapter

app = FlaskAdapter.create_app(config: dict = None)
```

- **Methods**:
  - `create_app(config: dict = None) -> Flask`
    - Creates and configures a Flask application with Gatria routes.

### Django Adapter

```python
from Gatria.adapters.django import DjangoAdapter

urlpatterns = DjangoAdapter.get_urls()
```

- **Methods**:
  - `get_urls() -> list`
    - Returns Django URL patterns for the Gatria app.

### FastAPI Adapter

```python
from Gatria.adapters.fastapi import FastAPIAdapter

app = FastAPIAdapter.create_app()
```

- **Methods**:
  - `create_app() -> FastAPI`
    - Creates a FastAPI application with Gatria routes.

---

## `Gatria.database` Module

Provides database integration layers.

### SQLAlchemy Database

```python
from Gatria.database.sqlalchemy import SQLAlchemyDatabase

db = SQLAlchemyDatabase(connection_string: str)
```

- **Parameters**:
  - `connection_string` (str): Database connection URI.

### MongoDB Database

```python
from Gatria.database.mongodb import MongoDBDatabase

db = MongoDBDatabase(uri: str, db_name: str)
```

- **Parameters**:
  - `uri` (str): MongoDB connection URI.
  - `db_name` (str): Database name.

---

## `Gatria.ml` Module

Machine Learning utilities for analytics.

### `EmployeeAnalytics` Class

Provides methods for generating analytics and reports.

#### Methods

- `generate_performance_report(department: str = None) -> dict`
  - **Description**: Generates a performance report for a department or the entire organization.
  - **Parameters**:
    - `department` (str, optional): The department to generate the report for.
  - **Returns**: A dictionary containing analytics data.
  - **Example**:
    ```python
    analytics = EmployeeAnalytics()
    report = analytics.generate_performance_report(department='Engineering')
    ```

- `predict_employee_retention(data: dict) -> float`
  - **Description**: Predicts the likelihood of an employee staying with the company.
  - **Parameters**:
    - `data` (dict): Employee data for the prediction model.
  - **Returns**: A probability score between 0 and 1.
  - **Example**:
    ```python
    retention_probability = analytics.predict_employee_retention(employee_data)
    ```

---

## Additional Modules

- `Gatria.utils`: Utility functions and helpers.
- `Gatria.exceptions`: Custom exception classes used within the system.

---

## Examples

Refer to the [Examples and Tutorials](./examples.md) document for practical usage examples.