import pickle
import pprint as pp


def Update_marks(data):
    data = {}
    found = False
    reader = int(input("Enter the Roll No. to update: "))
    file = open("Student.pickle", 'rb+')

    try:
        while True:
            pos = file.tell()
            data = pickle.load(file)
            if data["Roll"] == reader:
                print("Record Found")
                print(data)
                data["Marks"] = float(input("Enter the marks: "))
                file.seek(pos)
                found = True
                pickle.dump(data, file)
                break
    except EOFError:
        if found == False:
            print("Record not found \n \n")
        else:
            print("Marks updated Sucessfully")
        file.close()

