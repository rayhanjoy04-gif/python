arr = [10, 20, 30, 40, 50]

target = int(input("Enter target: "))

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        print("Target found at index", mid)
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Target not found")