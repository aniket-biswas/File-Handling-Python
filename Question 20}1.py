def ATOEDISP():
    f = open('NEWS.TXT')
    for line in f:
        s = line.split() 
        for word in s:
            if 'computar' in word.lower(): 
                word=word.replace('A','E')
            print(word,end=' ')
ATOEDISP()
