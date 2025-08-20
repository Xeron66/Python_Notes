# A generic way to catch all exceptions!
a = 10
b = "two"
# This type of exception handling is generic
# and can handle any type of exception it gets 
# during run time!
try:
    result = a / b
except Exception as e:
    print(f'Exception: {e}')

# A specific way to catch an Exception!
n = 10
m = 0

# This type of exception handling is very specific!
try:
    result = n / m
except ZeroDivisionError:
    print("Cant be divided by Zero!")