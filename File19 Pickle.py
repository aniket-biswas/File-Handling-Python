import pickle
f = open('student.dat','rb')
while True:
    try:
        rec = pickle.load(f)
        print('Roll Num:',rec['Rollno'])
        print('Name:',rec['Name'])
        print('Marks:',rec['Marks'])
    except EOFError:
        break
f.close()   