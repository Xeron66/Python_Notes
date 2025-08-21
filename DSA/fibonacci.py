# implementing the fibonacci series using "for loops"
# ---------------------------------------------------------

# storing the first 2 values i.e., 0 1
prev1 = 0
prev2 = 1

# n is the steps here
n = 18

# printing the first 2 values 0 1 of fibonacci series
print(prev1)
print(prev2)

# loop to handle the series progression
# since I am already printing the first 2 values
# the loop starts at the 3rd index! thats why n+1
for i in range(3, n+1):
    newFibo = prev1 + prev2
    print(newFibo)
    prev1 = prev2
    prev2 = newFibo

# implementing the fibonacci series using "recursion"
# ---------------------------------------------------------

def myFibo(n):
    # less than 0 checking! 
    if n < 0:
        print("Only Positive Integers are allowed!!")
    # if n is 0 or 1 the function will print it straight
    # rather than going into recursion again
    if n == 0 or n == 1:
        return n
    else:
        return myFibo(n-1) + myFibo(n-2)
        # this is the formula F(n) = F(n-1) + F(n-2)

# just a loop to run through and print!
for i in range(0,18):
    print(f'{myFibo(i)}', end=" ") # used end = " " to print it horizontally!