arr = [10, 20, 30, 40, 50]

# Printing the whole list!
print(f'Arr: {arr}')

print("-----------------------------")
# Searching using index
print(f'First element: {arr[0]}')
print(f'Last element: {arr[4]}')

print("-----------------------------")
# Searching using value
print(f'Value: 40 is at index: {arr.index(40)}')

print("-----------------------------")
# Insertion
arr.insert(2, 60)
print(f'Arr: {arr}')

print("-----------------------------")
# Deletion
arr.remove(60)
print(f'Arr: {arr}')

print("-----------------------------")
# Sorting a list (built in method)
arr2 = [2,1,6,4,8,7,3]
arr2.sort()
print(f'Sorted Arr2: {arr2}')

print("-----------------------------")
# Reversing a list (built in method)
arr2.reverse()
print(f'Reversed Arr2: {arr2}')

print("-----------------------------")
# reversing using slicing method!
newArr2 = arr2[::-1]
print(f'NewArr2: {newArr2}')


