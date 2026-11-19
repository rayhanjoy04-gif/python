with open("file.txt","r") as f:
    data=f.read()
    print(data)
with open("file.txt","w") as f:
    f.write("Hello World")
    print(data)