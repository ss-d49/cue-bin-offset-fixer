import re, subprocess, sys, argparse

infile = "XBOARDS.bin"
sectors = [	266756784,
			51619344,
			40520256,
			32448192,
			31241616,
			52404912,
			51431184,
			49606032,
			34071072,
			26626992,
			8740032,
			7300608,
			8716512,
			10184160 ]

x=1
offset=0

for i in sectors:
	subprocess.call(['dd', f'if={infile[:-4]}.bin', f'of={infile[:-4]} (Track {x}).bin', f'skip={offset}', f'count={i}', 'iflag=skip_bytes,count_bytes'])
	x += 1
	offset += i

