# Two different ways of opening a file in python!
# Using the usual open and close way!
# OR using via "with" statement!

# Reading a file!
try: 
    file = open("file_handling/text.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file doesnt exists!")
finally:
    file.close() 
    # Note: I am using finally so that even if there is an
    # exception, the file will be closed!

# This is to just separate the two printing outputs!
print("----------------------------")


# But using "with" statement, python automatically closes the file
# which stops data leaks!
# This is the BEST PRACTICE!!!
try:
    with open("file_handling/text.txt","r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f'Error: {e}')





    