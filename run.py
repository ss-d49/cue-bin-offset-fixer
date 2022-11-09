import re
import subprocess
import sys
import argparse
import hashlib
from pathlib import Path
import os
import time

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

def hash_sha1_bytes(bytes):
    try:
        sha1 = hashlib.sha1()
        sha1.update(bytes)
        return sha1.hexdigest()
    except Exception as e:
        print(e)

def load_file_chunk(input_file_path, skip, count):
    file = Path(input_file_path)
    try:
        if file.exists():
            f = open(file, 'rb')
            f.seek(skip)
            chunk = f.read(count)
            return chunk
        else:
            print(f"File does not exist at: {file}")
    except Exception as e:
        print(e)

def load_file(input_file_path):
    buf_size = 65536  # 64kb chunks
    file = Path(input_file_path)
    try:
        if file.exists():
            return open(file, 'rb').read()
        else:
            print(f"File does not exist at: {file}")
    except Exception as e:
        print(e)

infile = "Space Channel 5 (Japan).bin"
sectors = 2088576
x = 2
offset = 1992144
finished = False

f = load_file(infile)

while not finished:
    # subprocess.call(['dd', f'if={infile}', f'of=Track {x}.bin',
    #                 f'skip={offset}', f'count={sectors}', 'iflag=skip_bytes,count_bytes'])
    # ho = hash_sha1(f'Track {x}.bin')
    # print(ho, offset)

    #ch = load_file_chunk(infile,offset,sectors)
    ch = f[offset:offset+sectors]
    h = hash_sha1_bytes(ch)
    print(h, offset, end='\r')
    if h == "0ecd537e42946f3e74c80c9fcb8d0bccccfc96f1":
        print(offset)
        finished = True
    else:
        offset += 1
