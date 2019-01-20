import json
from functools import wraps

def to_json(get_data):
    @wraps(get_data)
    def wrapped(*args, **argv):
        return json.dumps(get_data(*args, **argv))
    return wrapped

@to_json
def get_data(x,y):
    return {
        x: y
    }


print(get_data(10, 5))
