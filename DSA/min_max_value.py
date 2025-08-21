arr = [7, 3, 6, 2, 5]
minVal = arr[0]
maxVal = arr[0]

for i in arr:
    if i < minVal:
        minVal = i
    elif i > maxVal:
        maxVal = i

print(f'Smallest Value: {minVal}')
print(f'Greatest Value: {maxVal}')
