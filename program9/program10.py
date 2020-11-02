'''
Write a Python program to implement a List using a list data-structure.
'''
import sys

LIST = []

def add(index,obj):
    LIST.insert(index,obj)


def delete(elememt):
    LIST.remove(elememt)


def search(obj):
    for i in range(len(LIST)):
        if LIST[i] == obj:
            print(f"Object found at {i} index")


while True:
    print('''\n1. Insert a value into the LIST
2. Append a value to the list
3. Delete a value from the LIST
4. Display the LIST
5. Search the LIST for an element 
6. Exit
    ''')
    choice = int(input("Enter a choice: "))


    if choice == 1:
        OBJECT = input("Element: ")
        INDEX = int(input("Index: "))
        add(INDEX,OBJECT)


    elif choice == 2:
        VAR = input("Element to append: ")
        LIST.append()


    elif choice == 3:
        ELEMENT = input("Enter the element to remove: ")
        try:
            delete(ELEMENT)
        except ValueError:
            print("ELement not present in the list")


    elif choice == 4:
        print(LIST)


    elif choice == 5:
        OBJ = input("Enter the element to search: ")
        search(OBJ)


    elif choice == 6:
        sys.exit()
