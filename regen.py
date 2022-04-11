import re, subprocess, sys, argparse
import hashlib, os
import time

def hash(file):
	BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
	with open(file, 'rb') as f:
		while True:
			data = f.read(BUF_SIZE)
			if not data:
				break
			return hashlib.sha1(data).hexdigest()
			
infile = "ROCKCLIMB.bin"
sectors = 31241616
x = 9
offset = 391344576
offset -= 48
finished = False

while not finished:
	subprocess.call(['dd', f'if={infile}', f'of=Track {x}.bin', f'skip={offset}', f'count={sectors}', 'iflag=skip_bytes,count_bytes'])
	h=subprocess.check_output(['sha1sum', 'Track 9.bin']).decode("utf-8")
	print(str(h[:-14]), offset)
	if str(h[:-14])=="333b4e25b086f23fdc66ad67d824f0c1f4754760":
		print(offset)
		finished = True
	else:
		offset += 1