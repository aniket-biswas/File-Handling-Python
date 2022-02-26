def UpperCase():
    f = open('poem.txt') 
    count = 0
    for line in f:
            if line[0].isupper():
                count+=1
    print("Lines starting from Capital letters: ",count)
UpperCase()
