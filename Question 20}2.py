def ATOEDISP():
    f = open('NEWS.TXT')
    s=f.read()
    for ch in s:
        if ch.lower() == 'a':
            print("E",end="")
        else:
            print(ch,end="")
ATOEDISP()
