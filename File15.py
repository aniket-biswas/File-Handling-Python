f = open("a7.txt", 'w')
str = 'Aniket\nBiswas'
f.write(str)
f.close()

f = open("a7.txt", 'a+')
f.write("\nThank You")
f.close()

f = open("a7.txt", 'r')
text = f.read()
print(text)
f.close()