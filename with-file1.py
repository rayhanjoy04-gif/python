with open("file1.txt","r")as f:
    data =f.read()
    new_data=data.replace("java","python")
print(new_data) 
with open("file1.txt","w")as f:
    f.write(new_data)   