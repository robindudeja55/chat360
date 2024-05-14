import os
from flask import Flask
class Config:
    DEBUG = True
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'IAMrobin10!')
    DB_NAME = os.environ.get('DB_NAME', 'chat360')
