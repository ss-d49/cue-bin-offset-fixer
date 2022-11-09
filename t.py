import hashlib
from pathlib import Path

def hash_sha1(input_file_path):
    """Calculate a hash from a file.
    Returns hash calculated from the file.
    """
    buf_size = 65536  # 64kb chunks
    file = Path(input_file_path)
    try:
        if file.exists():
            sha1 = hashlib.sha1()
            f = open(file, 'rb')
            while chunk := f.read(buf_size):
                sha1.update(chunk)
            return sha1.hexdigest()
        else:
            print(f"File does not exist at: {file}")
    except Exception as e:
        print(e)

h2 = hash_sha1(f'1.bin')
print(h2)
