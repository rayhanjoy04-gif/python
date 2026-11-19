nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7

lb = 0
hb = len(nums) - 1
result = -1 

while lb <= hb:
    mid = (lb + hb) // 2
    if nums[mid] == target:
        result = mid
        break
    elif nums[mid] < target:
        lb = mid + 1
    else:
        hb = mid - 1

if result != -1:
    print("ITEM is found!!")
else:
    print("ITEM is not found!!")