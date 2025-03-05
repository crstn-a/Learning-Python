#variables references/assign to a certain value

message = "Hello Python World!"
print (message)

message = "Hello Python Crash Course World!"
print(message)

#string

test_string = "This is a string with 'single quotes' and \"double quotes\""
print(test_string)

name = "Ada Lovelace"
print(name.title())

name = "Tin "
message = f"Hello {name.title().strip()}, would you like to learn some Python today?"
#strip is used if you want to remove whitespaces both left and right.
print (message)

name = " Ada Lovelace "
name.rstrip() #removes whitespace from the right side
name.lstrip() #removes whitespace from the left side
name.strip() #removes whitespace from both sides

name = name.strip()
print (name)

print ("\tIf you never try you'll never know.")

#Example URL
example_url = "https://www.google.com"
print(example_url.removeprefix("https://"))
#remove prefix is removing the filetype that is being used to solely focus on the name itself of the file.


filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
#remove suffix is removing the filetype that is being used to solely focus on the name itself of the file.

name = "ada lovelace"
print(name.title()) 

# The output of the code would be Ada Lovelace. 
# The title method would change the first letter of each word to uppercase.

print (name.upper())
print (name.lower())

message = f"Hello, my name is {name.title()}" # f-string is a formatted string literal that are like %s in C
print (message)

# \t = tab
# \n = new line
print ("Languages:\n\tPython\n\tC#\n\tJava")

#Apostrophe
message_ap = "Python's syntax is easy to learn."
print(message_ap)

