f = open("a4.txt", 'r')
for text in f.readlines():
    print(text)
f.close()