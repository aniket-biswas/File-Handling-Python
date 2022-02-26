a = open("a1.txt","r")
n=int(input("Enter No:"))
for i in range(n):
    nline=a.readline()
    print(nline,end="")
a.close()