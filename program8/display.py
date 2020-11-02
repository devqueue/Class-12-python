import pickle
import pprint as pp

def Display(data):
    data = {}
    file = open("Student.pickle", 'rb')
    try:
        while True:
            Student = pickle.load(file)
            pp.pprint(Student)
    except EOFError:
        file.close()

