import datetime;
import os;
import sys;

# only one argument when used from cmd line. (relative path)
relativePath = ''
if len(sys.argv) > 1:
	relativePath = sys.argv[1]




ct = datetime.datetime.now()
ct = str(ct)
output = 'media ' + ct +'.txt'

with open(output, 'w') as f:
	line = '_________________________________________________________________________________'

	dirName = 'Movies'
	directory = relativePath + dirName
	files = []
	f.write("\n" + line + "\n")
	f.write(dirName + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")



	dirName = 'Movies 4K'
	directory = relativePath + dirName
	files = []
	f.write("\n" + line + "\n")
	f.write(dirName + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")


	dirName = 'TV'
	directory = relativePath + dirName
	files = []
	f.write("\n" + line + "\n")
	f.write(dirName + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")


	dirName = 'TV 4K'
	directory = relativePath + dirName
	files = []
	f.write("\n" + line + "\n")
	f.write(dirName + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")



