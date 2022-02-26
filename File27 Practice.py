print("PLEASE ENTER NEGATIVE NO")
n=int(input("enter no:"))
a = open("a1.txt", "r")
l=a.readlines()
lastl=l[n:]
print(lastl)
a.close()