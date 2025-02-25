# Gatria v0.1.1 Release Notes

[![PyPI version](https://badge.fury.io/py/gatria.svg)](https://badge.fury.io/py/gatria)
[![Python Support](https://img.shields.io/pypi/pyversions/gatria.svg)](https://pypi.org/project/gatria/)
[![License](https://img.shields.io/github/license/Kanopusdev/Gatria.svg)](https://github.com/Kanopusdev/Gatria/blob/main/LICENSE)

Gatria continues to evolve as a comprehensive employee management system with this maintenance and enhancement release. Version 0.1.1 brings improved framework compatibility, additional database support, and enhanced development tools.

**Key Features Remain:**
- Attendance Tracking
- Leave Management
- Performance Tracking
- Multi-framework Integration
- Configurable Settings

**What's New in 0.1.1:**

- **Enhanced Web Framework Support:**
  - Added Werkzeug integration for improved Flask compatibility
  - Introduced Django REST Framework support for better API development
  - FastAPI and Uvicorn support for modern async web applications

- **Expanded Database Integration:**
  - Added PostgreSQL support via psycopg2-binary
  - Redis integration for caching and quick data access
  - Improved SQLAlchemy and MongoDB connectivity

- **Developer Experience:**
  - Added comprehensive testing tools (pytest-cov, tox)
  - Enhanced CI/CD pipeline with automated PyPI publishing
  - Improved package organization with optional dependency groups

- **Optional Modules:**
  - Reorganized dependencies into focused groups (web, database, async, ml)
  - Machine learning capabilities now available as optional installs
  - Reduced base installation footprint

**Installation Options:**

Basic installation:
```bash
pip install gatria
```

Feature-specific installations:
```bash
pip install gatria[web]      # Web framework support
pip install gatria[database] # Database integrations
pip install gatria[async]    # Async capabilities
pip install gatria[ml]       # Machine learning features
pip install gatria[dev]      # Development tools
```

**Quick Start:**
```python
from gatria import AttendanceTracker, LeaveManagement
from gatria.web import FlaskAdapter

# Initialize with Flask
app = FlaskAdapter()
tracker = AttendanceTracker()
leave_mgmt = LeaveManagement()

# Setup routes
@app.route('/check-in', methods=['POST'])
def check_in():
    return tracker.check_in(employee_id=request.json['employee_id'])

@app.route('/request-leave', methods=['POST'])
def request_leave():
    return leave_mgmt.request_leave(
        employee_id=request.json['employee_id'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date']
    )
```

**Breaking Changes:**
- None in this release

**Bug Fixes:**
- Fixed dependency conflicts in web framework integrations
- Improved error handling in database adapters
- Resolved async context management issues

**Documentation:**
- Updated installation guides for optional features
- Added more code examples
- Improved API documentation

For complete documentation, visit our [GitHub repository](https://github.com/Kanopusdev/Gatria).

## Support

For issues and feature requests, please use our [GitHub Issues](https://github.com/Kanopusdev/Gatria/issues) page.

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
