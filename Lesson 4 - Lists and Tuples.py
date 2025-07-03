# make a list, a collection of items, by putting them in square brackets seperated by a comma
my_list = ["This", "makes", "a", "list"]
print(my_list)
print(type(my_list))
print(" ")
# There are different ways to format how a list is printed
# Both of these methods specify how to seperate the items
print(*my_list, sep=' ')
print(" ")
# Above - seperated by a space, below - seperated by a new line
print('\n'.join(my_list))
print(" ")
# You can specify a particular item in the list to print. Remember, it starts count at 0
# So 0 would be the first item, 1 is second etc.
print(my_list[0])
 
# A negative number counts from the end, with -1 being the last item
print(my_list[-1])

# A Tuple is like a list, but established with () instead of [], and cannot be changed
# This makes it 'immutable'
my_tuple = ("my", "first", "tuple")
print(my_tuple)
print(type(my_tuple))