# Sorting by bubble sort method
# basically using two loops to iterate
# we are taking a temp var to replace

arr = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(arr)

for i in range (n-1):
    for j in range (n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
print(arr)

# --------------------------------------------------
# Improvement of bubble sort

# 1 issue is that in the best case scenario, 
# when the lowest value is at the left most side
# the swapping is done once yet the loop keeps on running

arr = [7, 3, 9, 12, 11]

n = len(arr)

for i in range (n-1):
    swapped = False
    for j in range (n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            swapped = True
        if not swapped:
            break

print(arr)