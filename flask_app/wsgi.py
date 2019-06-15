import sys

sys.path.insert(0, '/home/ubuntu/testing_workshop/')
from flask_app.app import app as application

if __name__ == "__main__":
    application.run()
