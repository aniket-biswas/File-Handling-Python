def COUNT():
    f=open("REPEATED.txt")
    count=0
    for line in f:
        words=line.split()
        for w in words:
            if w.lower()=="catholic" or w.lower()=="mother":
                count+=1
    print("Count of catholic or mother is",count)
COUNT()