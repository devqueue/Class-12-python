import pickle


def Search(data):
    data = {}
    file = open("Student.pickle", 'rb+')
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
        if found == False:
            print("Record not found \n \n")
        file.close()


