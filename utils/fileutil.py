import json


def read_from_file(filename):
    try:
        f = open(filename, "r")
        print(json.loads(f))
    except Exception as err:
        print(f"{err}")
    else:
        return []
