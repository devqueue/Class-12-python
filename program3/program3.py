'''
Write a Python program to read a text file ( story.txt) line by line and print it.
'''

story = "story.txt"
with open(story, "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

