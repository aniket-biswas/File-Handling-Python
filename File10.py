f = open("a5.txt", 'r')
for text in f.readlines():
    for word in text.split( ):
        print(word)
f.close()