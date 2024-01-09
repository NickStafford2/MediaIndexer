import os;
import datetime;

ct = datetime.datetime.now()
ct = str(ct)
output = 'media ' + ct +'.txt'

with open(output, 'w') as f:
	line = '_________________________________________________________________________________'

	directory = 'Movies'
	files = []
	f.write("\n" + line + "\n")
	f.write(directory + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")



	directory = 'Movies 4K'
	files = []
	f.write("\n" + line + "\n")
	f.write(directory + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")


	directory = 'TV'
	files = []
	f.write("\n" + line + "\n")
	f.write(directory + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")


	directory = 'TV 4K'
	files = []
	f.write("\n" + line + "\n")
	f.write(directory + "\n\n")
	for filename in os.listdir(directory):
		files.append(filename);
	files.sort()
	for file in files:
		f.write(file + "\n")



