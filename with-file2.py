word="learning"
with open("demo.txt","r")as f:
    data =f.read()
    if(data.find(word)==-1):
        print("word not found")
    else:
        print("word found")