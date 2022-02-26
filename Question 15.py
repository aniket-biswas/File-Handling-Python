def Corona():
    f=open("poem.txt","r")
    count=0
    for line in f:
        words=line.lower().split()
        count+=words.count("corona")
    print("Corona Count:",count)
Corona()