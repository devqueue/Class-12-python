'''
Write a Python program to remove all the lines that contain the character 'a' in a text file (Content.txt)
and write it to another file(Newfile.txt).
'''

oldfile = open('content.txt')
lines = oldfile.readlines()
newopen = open('newfile.txt', 'w')
#print(lines)

for line in lines:
    if 'a' in line:
        #print(line)
        line = line.replace(line, '')
    else:
        newopen.write(line)
newopen.close()
oldfile.close()
