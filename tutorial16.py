file = open('file.txt', 'r')
f = file.readlines()

filelist = []
for line in f:
    filelist.append(line.strip())

print(filelist)