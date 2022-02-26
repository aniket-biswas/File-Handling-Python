f1 = open("a1.txt")
f2 = open("a2","w")
for line in f1:
     if 'a' not in line:
          f2.write(line)
print('File Copied Successfully!')
f1.close()
f2.close()

f2 = open("a2.txt","r")
print(f2.read())