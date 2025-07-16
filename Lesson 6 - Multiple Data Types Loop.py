# Make a list of different data types
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# using a loop means only one line needs to be written, 
# formatting in the variable 'item' goes through each item in list in order for each iteration of the loop
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))


# same can be done with the mixed dictionary from lesson 5
new_dictionary = dict(key = "Value", list_key = ["one", "two", "three"], integer = 1)
print("\n")

# 'k' and 'v' represent key and value for each item in the list
# \033[4m underlines, ''1m = bold, ''0m turns back to normal text]
for k, v in new_dictionary.items():
    print(f"\033[4m\033[1m{k}\033[0m is of the data type {type(v)}")
    
