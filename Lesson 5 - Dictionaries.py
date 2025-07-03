# A dictionary is like a list, but each item, known as a key, has a corresponding value
my_dictionary = {
  "key1" : "value1",
  "key2" : "value2",
  "key3" : "value3"
}
print(my_dictionary)
print(type(my_dictionary), "\n")

# A dictionary uses curly brackets {}, but it's also possible to create a dictionary with this method, 
# (you can also use different data types within a dictionary, not just strings)
new_dictionary = dict(key = "Value", list_key = ["one", "two", "three"], integer = 1)
print(new_dictionary, "\n")

# Print all the keys this way
print(my_dictionary.keys())

# And values like this 
print(my_dictionary.values())

# or print a specific key and its values
print(my_dictionary["key1"],"\n")

# Remember, dictionaries cannot have duplicate keys. A key of the same name will overwrite the old one
example = {
  "key1" : "unique",
  "key2" : "this will disappear",
  "key2" : "this will overwite key2"
}
print(example.values())



