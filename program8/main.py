'''
Write a Python program to create a binary file with roll number , name and marks. Input a roll number
and update the marks.
'''
import pickle
import sys
import pprint as pp
from writefile import write_in_file
from display import Display
from search import Search
from update import Update_marks

Sdata = {}


#main program
while True:
    print("Menu \n 1-Write in a file \n 2-display \n 3-Search \n 4-Update Marks \n 5-exit")
    ch = int(input("Enter a Choice: "))
    if ch == 1:
        write_in_file(Sdata)
    if ch == 2:
        Display(Sdata)
    if ch == 3:
        Search(Sdata)
    if ch == 4:
        Update_marks(Sdata)
    if ch == 5:
        sys.exit()
