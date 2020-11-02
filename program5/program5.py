'''
Write a Python program to read a text file line by line and display each word seperated by a #.
'''

with open('story.txt', 'r') as f:
    for line in f:
        for word in line.split():
            print(word, end="#")
    print('\n')
