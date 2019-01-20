"""
import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key",  help="Key for a key-value_storage", type=str)
parser.add_argument("--val",  help="Value for a key-value_storage", type=str)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

json_decoded = dict()

if args.val == None:
    if os.path.exists(storage_path) == True:
        with open(storage_path, 'r+t') as f:
            json_decoded = json.load(f)
            needed_items = json_decoded[args.key]
            i = len(needed_items)
            for item in needed_items:
                print(f"{item}", end='')
                i -= 1
                if i > 0:
                    print(", ", end='')
    else: pass

else:
    if os.path.exists(storage_path) == True:
        with open(storage_path) as f:
            json_decoded = json.load(f)

        json_decoded.setdefault(args.key, []).append(args.val)

        with open(storage_path, 'w+t') as f:
            json.dump(json_decoded, f)
    else:
        json_decoded.setdefault(args.key, []).append(args.val)

        with open(storage_path, 'w+t') as f:
            json.dump(json_decoded, f)

"""

# faast_____________________________________________

import argparse
import json
import os
import tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def clear():
    os.remove(storage_path)


def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        clear()
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')