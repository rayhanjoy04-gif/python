arr = [10, 20, 30, 40, 50]

target = int(input("Enter target: "))

for i in range(len(arr)):
    if arr[i] == target:
        print("Target found at index", i)
        break
else:
    print("Target not found")