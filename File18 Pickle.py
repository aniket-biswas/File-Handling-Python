import pickle
rollno= int(input('Enter roll number:'))
name = input('Enter Name:')
marks = int(input('Enter Marks'))
#Creating the dictionary
rec = {'Rollno':rollno,'Name':name,'Marks':marks}
#Writing the Dictionary
f = open('student.dat','ab')
pickle.dump(rec,f)
f.close()