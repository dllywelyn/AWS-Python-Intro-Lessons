# 'print' allows following statement to be shown in terminal 
print("Hello world.")
print("This kind of text data is called a 'string'.")
print("Printed statements must go in quotations inside brackets.")

# but you don't have to use print for strings only
# below is a variable (stored data) which I've defined with a string value
no_quotes = "with no quotation marks needed"

# different printed items in one line must be seperated with commas
# strings go inside quotes, but no need for variables
print("You can also print variables like this -->", no_quotes)

# you don't have to print a string at all, you could only use variables if need
first_string = "You don't have to print a string directly, you could print a variable on its own"
print(first_string)
second_string = " and concatenate (add) two strings variables together"
print(first_string + second_string)
third_string = " like this"
# you can concatenate in print statemntes as above, or concatenate into a  new variable and print that as below
concatenated = first_string + second_string + third_string
print(concatenated)

# how to start new lines in your terminal and code
print("\nInstead of making different print statements for each line, \nyou can start new lines in one string")
print("And you can seperate lines in your code \
like this, which will look like one line in the terminal screen")
