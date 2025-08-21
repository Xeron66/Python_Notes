
prev1 = 0
prev2 = 1
n = 18

print(prev1)
print(prev2)
for i in range(n):
    newFibo = prev1 + prev2
    print(newFibo)
    prev1 = prev2
    prev2 = newFibo