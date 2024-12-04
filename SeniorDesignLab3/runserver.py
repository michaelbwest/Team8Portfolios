"""
This script runs the SeniorDesignLab3 application using a development server.
"""

from email.mime import application
from os import environ
from app import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    app.run(HOST, PORT)

