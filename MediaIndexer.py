import datetime;
import os;
import sys;

# only one argument when used from cmd line. (relative path)
relativePath = ''
if len(sys.argv) > 1:
	relativePath = sys.argv[1]


	line = '_________________________________________________________________________________'

def WriteDir(dirName: str):
	directory = relativePath + dirName
	files = []
	f.write("\n" + line + "\n")
	f.write(dirName + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")


ct = datetime.datetime.now()
ct = str(ct)
output = 'media ' + ct +'.txt'

with open(output, 'w') as f:
	WriteDir("Movies")
	WriteDir("Movies 4K")
	WriteDir("TV")
	WriteDir("TV 4K")