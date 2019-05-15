import re
import sys

flags = sys.argv[2:]
songs = []
base_address = ''

with open(sys.argv[1], 'r') as songlist:
	lines = songlist.readlines()
	base_address = lines[0][:-1]
	for line in lines[1:]:
		songs.append(re.sub('(?m) *\t.*\n?', '', line[1:]))
		
if('--dry' in flags):
	for song in songs:
		print(base_address + song)	
else:
	with open('song_addresses.txt', 'w') as addresses:
		for song in songs:	
			addresses.write(song + '\n')