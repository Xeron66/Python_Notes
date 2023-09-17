# list is a varsatile compound data type, contains heterogenous data types, upgradeable, square bracets are used '[]'
my_list = ['Foyez', 2013122042, 'ECE']

print('These are the data of List')
for i in range(0, 3):
    print(my_list[i])

print('\n\n')

# tuples are like lists, uses parenthesis '()', and cannot be updated
my_tuple = ('Foyez', 2013122042, 'ECE')

print('These are the data of Tuple')
for i in range(0,3):
    print(my_tuple[i])
print('\n\n')


# dictionary type uses a key and a value
my_dict = {'name:': 'Foyez', 'Id:': 203122042, 'Department:': 'ECE'}

print('These are the data of dictionary')
print('Print with colon')
for key, value in my_dict.items():
    print(key, value)

print('\n\n')

print('Print without colon')
# To print this without the colons i.e., name: => name= use the following code
for key, value in my_dict.items():
    print(key.strip(':'), '=', value)