list=[1,2,4,8,16,32,64,128,256,512]
item=int(input("Enter a number: "))
i=0
while i<len(list):
    if list[i]==item:
        print("Item found at index",i)
    else:
        print("Item not found at index",i)
    i+=1