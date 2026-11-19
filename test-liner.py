LA=[30,50,70,90,40]

Target=70

""" List=[]
for j in range(5):
    x=int(input("Enter number: "))
    List.append(x)
"""
for i in range(len(LA)):
    if LA[i]==Target:
       print("Found",LA[i])
       break
else:
    print("Not Found")    


