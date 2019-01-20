import tempfile
import os

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as fp:
    fp.write('dfsfsd')
with open(storage_path, 'r') as fp:
    fp.seek(0)
    print(fp.read())