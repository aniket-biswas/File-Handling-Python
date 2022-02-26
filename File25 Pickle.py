import pickle
f = open('student.dat','rb')
reclst= []
r=int(input("Enter roll no to be deleted:"))
while True:
    try:
        rec = pickle.load(f)
        reclst.append(rec)
    except EOFError:
        break
f.close()
f = open('student.dat','wb')
for x in reclst:
    if x['Rollno']==r:
        continue
    pickle.dump(x,f)
f.close()