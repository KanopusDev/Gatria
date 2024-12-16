import asyncio
from datetime import datetime, timedelta
from employee_management import AttendanceTracker, LeaveManagement, PerformanceTracker, LeaveStatus, ConfigManager, ValidationError, AdapterFactory


async def main():
    try:
        # Initialize configuration
        config_manager = ConfigManager("config.json")
        
        # Initialize core systems
        attendance = AttendanceTracker(config_manager)
        leave = LeaveManagement(config_manager)
        performance = PerformanceTracker(config_manager)

        # 1. Web Framework Integration Example
        web_adapter = AdapterFactory.create_adapter('web', 'flask')
        web_adapter.initialize(debug=True)
        
        # Add a test route to the Flask app
        @web_adapter.app.route('/test')
        def test_route():
            return {'message': 'Test route'}
        
        # Example web endpoint handling
        api_data = {"employee_id": "EMP001", "status": "login"}
        with web_adapter.app.app_context():
            web_response = web_adapter.handle_data(api_data)
            print("Web Response:", web_response)

        # 2. Database Integration Example
        db_adapter = AdapterFactory.create_adapter('database', 'sqlalchemy')
        db_adapter.initialize(connection_string='sqlite:///employee.db')
        
        # Example database operation
        employee_data = {
            "id": "EMP001",
            "name": "John Doe",
            "department": "IT"
        }
        db_response = db_adapter.handle_data(employee_data)
        print("Database Operation:", db_response)

        # 3. Async Operations Example
        async_adapter = AdapterFactory.create_adapter('async', 'aiohttp')
        async_adapter.initialize()
        
        # Example async operation
        async_data = {
            "task": "process_payroll",
            "employee_ids": ["EMP001", "EMP002"]
        }
        async_result = await async_adapter.handle_data(async_data)
        print("Async Operation Result:", async_result)

        # 4. Machine Learning Integration Example
        ml_adapter = AdapterFactory.create_adapter('ml', 'sklearn')
        ml_adapter.initialize()
        
        # Example ML prediction
        performance_data = {
            "attendance_rate": 0.95,
            "tasks_completed": 150,
            "quality_score": 4.8
        }
        prediction = ml_adapter.handle_data(performance_data)
        print("ML Prediction:", prediction)

        # 5. Core System Operations
        employee_id = "EMP001"

        # Attendance tracking
        try:
            attendance.log_entry(employee_id, "login")
            print("Attendance logged successfully")
        except ValidationError as e:
            print(f"Attendance error: {e}")

        # Leave management
        try:
            start_date = datetime.now() + timedelta(days=5)
            end_date = start_date + timedelta(days=2)
            leave_request = leave.request_leave(
                employee_id, 
                start_date, 
                end_date, 
                "Vacation"
            )
            print(f"Leave requested successfully: {leave_request}")
        except ValidationError as e:
            print(f"Leave request error: {e}")

        # Performance tracking
        try:
            performance_data = {
                "task_completion": 95,
                "quality_score": 4.8,
                "feedback": "Excellent work",
                "rating": 4.8,
                "reviewer_id": "MANAGER01"
            }
            performance.record_performance(employee_id, performance_data)
            print("Performance recorded successfully")
        except ValidationError as e:
            print(f"Performance tracking error: {e}")

    except Exception as e:
        print(f"System error: {e}")
        raise

def run_example():
    # Fix for deprecation warning in Python 3.12+
    try:
        # For Python 3.12+
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    except AttributeError:
        # Fallback for older Python versions
        loop = asyncio.get_event_loop()
    
    try:
        loop.run_until_complete(main())
    except Exception as e:
        print(f"Error running example: {e}")
        raise
    finally:
        loop.close()

if __name__ == "__main__":
    run_example()
