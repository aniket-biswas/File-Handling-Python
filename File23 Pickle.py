import pickle
f = open('student.dat','rb')
flag = False
r=int(input("Enter rollno to be searched:"))
while True:
    try:
        rec = pickle.load(f)
        if rec['Rollno'] == r:
            print('Roll Num:',rec['Rollno'])
            print('Name:',rec['Name'])
            print('Marks:',rec['Marks'])
            flag = True
    except EOFError:
        break
if flag == False:
    print('No Records found')
f.close()