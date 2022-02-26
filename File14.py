import os
f=open("","r")
g=open("C:\Users\biswa\OneDrive\Desktop\Visual Studio Code\Python\Programming Class 12\Chapter 3 _ File Handling\a2.txt","w")
for text in f.readlines():
    text=text.replace('my','your')
    g.write(text)
f.close()
g.close()
os.remove("d:\\a.txt")
os.rename("d:\\c.txt","d:\\a.txt")
print("file contents modified")