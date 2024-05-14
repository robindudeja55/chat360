# chat360

to get logs:
curl -X GET http://127.0.0.1:5000/logs
to add logs:
curl -X POST -H "Content-Type: application/json" -d '{"level":"error", "log_string":"Example log message", "timestamp":"2024-05-14T17:30:00Z", "source":"log1.log"}' http://127.0.0.1:5000/logs



Chat360 Logs Management System is a simple Flask-based application for managing logs. It provides APIs to retrieve logs and add new logs to the system.

Prerequisites
Python 3.6 or higher
MySQL database
Flask
pymysql

Configuration
Set up the MySQL database:

Create a new MySQL database named 'chat360'.
Update the database connection settings in the config.py file if necessary.
Initialize the database schema:
Python db.py

Start the Flask application:

python main.py
The application will be accessible at http://127.0.0.1:5000.

Use the following endpoints to interact with the application:

GET /logs: Retrieve all logs from the database.
POST /logs: Add a new log to the database. Send a JSON payload with the log details (level, log_string, timestamp, source).
