'''
Write a Python program to create a binary file with name and roll number. Search for a given roll
number and display the name, if not found , display appropriate message.
'''
import pickle
import sys
import pprint as pp
dict= {}

def write_in_file():
    file = open("Student.pickle", "ab")
    dict["Roll"] = int(input("Enter the Roll NO: "))
    dict["Name"] = input("Enter a name: ")
    pickle.dump(dict, file)
    file.close()

def display():
    file = open("Student.pickle", 'rb')
    try:
        while True:
            Student = pickle.load(file)
            pp.pprint(Student)
    except EOFError:
        pass
    file.close()


def search():
    file = open("Student.pickle", 'rb')
    reader = int(input("Enter the Roll No. to search: "))
    found = False
    try:
        while True:
            data = pickle.load(file)
            if data["Roll"] == reader:
                print("Record Found")
                print(data)
                found = True
                break
    except EOFError:
        pass
    if found==False:
        print("Record not found \n \n")
    file.close()


#main program
while True:
    print("Menu \n 1-Write in a file \n 2-display \n 3-Search \n 4-exit \n")
    ch = int(input("Enter a Choice: "))
    if ch==1:
        write_in_file()
    if ch==2:
        display()
    if ch==3:
        search()
    if ch==4:
        sys.exit()
        

