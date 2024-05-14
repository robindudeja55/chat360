import pymysql.cursors
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_NAME'],
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    with current_app.app_context():
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    level VARCHAR(20) NOT NULL,
                    log_string VARCHAR(255) NOT NULL,
                    timestamp DATETIME NOT NULL,
                    source VARCHAR(50) NOT NULL
                )
            """)
        db.commit()
