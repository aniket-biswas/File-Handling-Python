def Two():
    f = open('poem.txt') 
    count = 0
    for line in f:
        words = line.split() 
        for w in words:
            if len(w)==2:
                print(w,end=' ')
Two()
