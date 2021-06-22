# Using and Managing Strings
# string casting
# string concatenation
# Casting methods

# single and double quotes
single_quotes = 'These are single quotes and working perfectly fine!'
double_quotes = "These are double quotes also working fine"

# print(single_quotes)
# print(double_quotes)

# Concatenation
# First_Name = "James"
# Last_Name = 'Bond'
# age = "18"
# # print(First_Name)
# # print(Last_Name)
# # print(First_Name + ' ' + Last_Name + ' ' + str(age)) # example of Concatenation and Casting
# print(type(age))
# print(type(int(age))) # example of casting string into an integer
# Create a variable called age with int value and display age in the same line as James Bond
# String slicing and Indexing

# In python Indexing starts with 0
        #    01234567891011
# greetings = "Hello World!"
#            #           -1
# print(greetings)
# # To confirm the length of this string we method called len()
#
# print(len(greetings))
#
# print(greetings[0:5]) # slicing the string from index 0  - 4 upto 5, slicing string right to left starting from 0
#
# print(greetings[-6:]) # slicing string lef to right starting from -1

# string built in methods

# white_spaces = "Lot's of white spaces                                                         "
# print(str(len(white_spaces)) + " including white spaces")
# # we have strip() that removes all the white spaces
# #print(white_spaces.strip())
# print(str(len(white_spaces.strip())) + " excluding white spaces ")


# some more built in methods that we can use with strings

example_text = "here's Some text with lot's of text"

print(example_text.count("text")) # count() method counts the word in the string
print(example_text.lower()) # brings everything to lower case
print(example_text.upper()) # brings everything to upper case
print(example_text.capitalize()) # capitalises the first letter in the string
print(example_text.replace("with", ","))

