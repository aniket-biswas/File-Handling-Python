import pickle
output_file= open("binary_file.bin","wb")
myint= 42
mystring= "Python.mykvs.in!"
mylist= ["python", "sql", "mysql"]
mydict= { "name": "ABC", "job": "XYZ" }
pickle.dump(myint, output_file)
pickle.dump(mystring, output_file)
pickle.dump(mylist, output_file)
pickle.dump(mydict, output_file)
output_file.close()
with open("binary_file.bin","wb") as f:
    while True:
        try:
            r=pickle.load(f)
            print(r)
            print("Next data")
    except EOFError:
        break
f.close()