def dispS():
    f = open('poem.txt') 
    count = 0
    for line in f:
        if line[0].lower()=='s':
            print(line)
dispS()
