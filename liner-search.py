arr = [10, 20, 30, 40, 50]

target = int(input("Enter a number to search: "))

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
        break
else:
    print("Not Found")