'''
Write a Python program to implement a stack using a list data-structure.
'''
import sys

STACK = []


def push(element):
    STACK.append(element)


def pop():
    if len(STACK) == 0:
        print("List is empty")
    else:
        c = STACK.pop()
        print(c)


def display_stack():
    for i in range(len(STACK)-1, -1, -1):
        print(STACK[i])

while True:
    print('''\n1. Push into the STACK
2. Pop value from the STACK
3. Display the STACK
4. Exit
    ''')
    choice = int(input("Enter a choice: "))
    if choice==1:
        val = input("Enter a value: ")
        push(val)
    elif choice==2:
        pop()
    elif choice==3:
        display_stack()
    elif choice == 4:
        sys.exit()
