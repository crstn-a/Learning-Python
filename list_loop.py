dogs = [
    'lucy',
    'sugar',
    'sweety',
    'negro'
]

#loop through dogs list
#to every each in the dogs list associate it with the variable 'dog'
for dog in dogs: 
    print(f"{dog.title()} is a very good dog.")
    print(f"I can't wait to see you {dog.title()} running in our own fields.\n")


#the only lines you should indent are the actions you want to repeat for each item in a for loop.

#doing this: will have an indentation error
#message = "Hello"
#    print(message)

favPizza = [
    "Hawaiian",
    "Pepperoni",
    "Cheese",
    "Ham"
]

for pizza in favPizza:
    print(f"I like {pizza} pizza!")

print("\nNow, I'm craving pizza!")