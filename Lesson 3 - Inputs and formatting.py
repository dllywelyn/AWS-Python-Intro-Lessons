# 'Print' will show data onscreen. Input is similar, with a key difference
print("This 'print' function shows a string. \nThe 'input' function also prints, \
but it's for statements that await a response")

# A 'print' statement doesn't need an answer, it just sits there.
# But an input needs ... well, input ...
input("This is printed as an input function, but you need to press a key (any) to continue")  
# Think of it like the difference between a statement and a question. 

print("You can define a variable as the answer to your input function")
response = input("Type 'Y' if you understand how 'input' works: ")
print(response)

# You can then take your input values and print them along with strings
string_question = input("What data type is a piece of text?  ")
input_question = input("Which function is used for asking the user a question?  ")
# After you define the input answers as variables, put them into a string.
# Previously we learnt to concatenate (add) using +
# But as below, we can put variables directly into string without having to concatenate
print("\nA {} is different to an {}".format(string_question, input_question))

# For a cleaner version, put f (for format) in front of the quotation mark
print(f"By putting 'f' in front of the {string_question}, \
I can put variables directly into {string_question}s and {input_question}s")