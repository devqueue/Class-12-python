import pickle

data = {}


def write_in_file(data):
    data = {}
    studs = int(input("Enter no. of students: "))
    file = open("Student.pickle", "rb+")
    for i in range(1,studs+1):
        data["Roll"] = int(input("Enter the Roll NO: "))
        data["Name"] = input("Enter a name: ")
        data["Marks"] = float(input("Enter the marks: "))
        pickle.dump(data, file)
        print(f"{i} Record(s) Entered Sucessfully")
        data={}
        
    file.close()



