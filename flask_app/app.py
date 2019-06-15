""" Quick Fibonacci API """

from flask import Flask
import logging
import json
import sys
import time

sys.path.insert(0, '/home/ubuntu/testing_workshop/')
from flask_app import fib

log = logging.getLogger('werkzeug')
log.disabled = True

app = Flask(__name__)


@app.route("/")
def hello():
    """ Hello world!"""
    return 'Hello World!'


@app.route("/fib/<number>", methods=['GET'])
def get_fib(number):
    """ Return Fibonacci JSON """
    return json.dumps(fib.get(int(number))), 200


@app.route("/wait/<number>", methods=['GET'])
def wait(number):
    """ Simple wait """
    time.sleep(int(number) / 10)
    return '{"wait": %d}' % (int(number) / 10)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
