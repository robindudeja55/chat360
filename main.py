# main.py

from flask import Flask, jsonify, request
from db import get_db, close_db, init_db
from datetime import datetime
app = Flask(__name__)
app.config.from_object('config.Config')

# Call init_db() function with app context

with app.app_context():
    init_db(app)

@app.route('/logs', methods=['GET'])
def get_logs():
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM logs")
        logs = cursor.fetchall()
    return jsonify(logs)


@app.route('/logs', methods=['POST'])
def add_log():
    data = request.get_json()
    level = data.get('level')
    log_string = data.get('log_string')
    timestamp_str = data.get('timestamp')  # Get timestamp string from JSON data
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")  # Parse timestamp string
    timestamp_formatted = timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Format timestamp as required by MySQL

    source = data.get('source')

    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO logs (level, log_string, timestamp, source) VALUES (%s, %s, %s, %s)", (level, log_string, timestamp_formatted, source))
        db.commit()
    return jsonify({'message': 'Log added successfully'}), 201

if __name__ == '__main__':
    app.run()
