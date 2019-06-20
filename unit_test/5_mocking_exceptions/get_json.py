import json


def get_json(filename):
    try:
        return json.loads(open(filename).read())
    except (IOError, ValueError):
        return ""

def