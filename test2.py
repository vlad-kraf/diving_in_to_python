import tempfile
import os
path = 'zzzzz'


new_path = os.path.join(tempfile.gettempdir(), path)

print(new_path)