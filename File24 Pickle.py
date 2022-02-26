import pickle
f = open('student.dat','rb')
reclst= []
r=int(input("Enter roll no to be updated"))
m=int(input("Enter correct marks"))
while True:
    try:
        rec = pickle.load(f)
        reclst.append(rec)
    except EOFError:
        break
f.close()
for i in range (len(reclst)):
    if reclst[i]['Rollno']==r:
        reclst[i]['Marks'] = m
f = open('student.dat','wb')
for x in reclst:
    pickle.dump(x,f)
f.close()