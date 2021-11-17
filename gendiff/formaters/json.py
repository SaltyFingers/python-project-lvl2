import json


def format_json(diff):

    """Returns formated difference between two files if json format

    arguments:
    diff: raw differene between two files"""

    return json.dumps(diff)
