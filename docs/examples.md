
# Examples and Tutorials

This document provides practical examples and tutorials to help you get started with the Gatria Employee Management System.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Web Framework Integration](#web-framework-integration)
  - [Flask Example](#flask-example)
  - [Django Example](#django-example)
  - [FastAPI Example](#fastapi-example)
- [Database Operations](#database-operations)
  - [Using SQLAlchemy](#using-sqlalchemy)
  - [Using MongoDB](#using-mongodb)
  - [Using Redis](#using-redis)
- [Asynchronous Operations](#asynchronous-operations)
- [Machine Learning Analytics](#machine-learning-analytics)
- [Advanced Usage](#advanced-usage)
  - [Custom Models](#custom-models)
  - [Extending Functionality](#extending-functionality)

---

## Quick Start

```python
from Gatria import EmployeeManager

# Initialize the EmployeeManager with default settings
manager = EmployeeManager()

# Create a new employee
employee_data = {
    "name": "John Doe",
    "position": "Software Engineer",
    "department": "Engineering",
    "email": "john.doe@example.com",
    "phone": "+1-555-0100",
    "date_hired": "2022-01-15"
}

employee = manager.create_employee(employee_data)

# Retrieve employee information
retrieved_employee = manager.get_employee(employee.id)
print(retrieved_employee.to_dict())

# Update employee data
updated_data = {"position": "Senior Software Engineer"}
manager.update_employee(employee.id, updated_data)

# Delete an employee
manager.delete_employee(employee.id)
```

---

## Web Framework Integration

### Flask Example

```python
from flask import Flask
from Gatria.adapters.flask import FlaskAdapter

app = Flask(__name__)
FlaskAdapter.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
```

**Instructions**:

1. Install the required packages:
   ```bash
   pip install Gatria[web]
   ```
2. Run the Flask application:
   ```bash
   python app.py
   ```

### Django Example

```python
# In your urls.py
from django.urls import path, include
from Gatria.adapters.django import DjangoAdapter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include(DjangoAdapter.get_urls())),
]
```

**Instructions**:

1. Install the required packages:
   ```bash
   pip install Gatria[web]
   ```
2. Update your `settings.py` to include the necessary configurations.
3. Run the Django application:
   ```bash
   python manage.py runserver
   ```

### FastAPI Example

```python
from fastapi import FastAPI
from Gatria.adapters.fastapi import FastAPIAdapter

app = FastAPI()
FastAPIAdapter.include_routes(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
```

**Instructions**:

1. Install the required packages:
   ```bash
   pip install Gatria[web]
   ```
2. Run the FastAPI application:
   ```bash
   uvicorn app:app --reload
   ```

---

## Database Operations

### Using SQLAlchemy

```python
from Gatria.database.sqlalchemy import SQLAlchemyDatabase
from Gatria import EmployeeManager

db = SQLAlchemyDatabase('sqlite:///employees.db')
manager = EmployeeManager(database=db)

# Create an employee
employee = manager.create_employee({
    "name": "Alice Brown",
    "position": "Project Manager",
    "department": "Operations",
})
```

**Instructions**:

1. Install SQLAlchemy:
   ```bash
   pip install sqlalchemy
   ```

### Using MongoDB

```python
from Gatria.database.mongodb import MongoDBDatabase
from Gatria import EmployeeManager

db = MongoDBDatabase('mongodb://localhost:27017/', 'Gatria_db')
manager = EmployeeManager(database=db)

# Create an employee
employee = manager.create_employee({
    "name": "Bob Smith",
    "position": "Data Analyst",
    "department": "Marketing",
})
```

**Instructions**:

1. Install PyMongo:
   ```bash
   pip install pymongo
   ```
2. Ensure MongoDB is running on your machine.

### Using Redis

```python
from Gatria.database.redisdb import RedisDatabase
from Gatria import EmployeeManager

db = RedisDatabase(host='localhost', port=6379)
manager = EmployeeManager(database=db)

# Create an employee
employee = manager.create_employee({
    "name": "Carol White",
    "position": "HR Manager",
    "department": "Human Resources",
})
```

**Instructions**:

1. Install Redis client:
   ```bash
   pip install redis
   ```
2. Ensure Redis server is running on your machine.

---

## Asynchronous Operations

```python
import asyncio
from Gatria import EmployeeManager

async def main():
    manager = EmployeeManager(async_mode=True)
    employee = await manager.create_employee_async({
        "name": "David Lee",
        "position": "DevOps Engineer",
        "department": "IT",
    })
    print(await manager.get_employee_async(employee.id))

asyncio.run(main())
```

**Instructions**:

1. Install asynchronous dependencies:
   ```bash
   pip install Gatria[async]
   ```
2. Run the script using an async-enabled environment.

---

## Machine Learning Analytics

```python
from Gatria.ml.analytics import EmployeeAnalytics

analytics = EmployeeAnalytics()

# Generate a performance report
report = analytics.generate_performance_report(department='Engineering')
print(report)

# Predict employee retention
employee_data = {
    "name": "Eve Adams",
    "position": "Sales Associate",
    "department": "Sales",
    "years_at_company": 2,
    "recent_performance_score": 4.5,
}
retention_probability = analytics.predict_employee_retention(employee_data)
print(f"Retention Probability: {retention_probability:.2f}")
```

**Instructions**:

1. Install machine learning dependencies:
   ```bash
   pip install Gatria[ml]
   ```
2. Ensure you have the necessary data for analytics.

---

## Advanced Usage

### Custom Models

You can extend the `Employee` model to include additional fields.

```python
from Gatria.models import Employee

class CustomEmployee(Employee):
    def __init__(self, skills, certifications, **kwargs):
        super().__init__(**kwargs)
        self.skills = skills
        self.certifications = certifications

# Usage
employee = CustomEmployee(
    id="emp789",
    name="Fiona Green",
    position="UX Designer",
    department="Design",
    skills=["Sketch", "Adobe XD"],
    certifications=["Certified UX Professional"]
)
```

### Extending Functionality

Implement custom functionality by extending existing classes.

```python
from Gatria.manager import EmployeeManager

class CustomEmployeeManager(EmployeeManager):
    def get_employees_by_department(self, department):
        # Implement custom logic to retrieve employees by department
        return [employee for employee in self.get_all_employees() if employee.department == department]

# Usage
manager = CustomEmployeeManager()
engineering_employees = manager.get_employees_by_department("Engineering")
for emp in engineering_employees:
    print(emp.name)
```

---