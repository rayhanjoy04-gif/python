Marks=int(input("Enter your marks: "))

if (Marks>=80):
    grads="A+"

elif (Marks>=70 and Marks<80):
    grads="A"

elif (Marks>=60 and Marks<70):
    grads="B"

elif (Marks>=50 and Marks<60):
    grads="C"

else:
    grads="Fail"

print("Your grads is:",grads)    