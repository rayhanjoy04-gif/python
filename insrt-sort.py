def insert_at_position(arr, key, k):
    arr.append(0)          
    j = len(arr) - 2       

    while j >= k:
        arr[j + 1] = arr[j]  
        j -= 1

    arr[k] = key
    return arr


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

key = 45
k = 7

print(insert_at_position(arr, key, k))