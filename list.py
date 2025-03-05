#List = sets of information that are store in one place.
#       can store elements of different data types (while array store must be same data type)
#       square brackets [] = indicate a list

my_lists = [1, "hello", 3.14, True]
print(my_lists)

#to access indiv element on the list while also using the string title method
print(f"Accessing the list, the value of index 1: {my_lists[1].title()}") 

#accessing the last element in the list
print(my_lists[-1])
# The index -2 returns the second item from the end of the list, -3 returns the third item, and so forth.


print("=== TRY IT YOURSELF ===")

bucket_list = [
    "Healthy body and Peaceful mind",
    "Not Perfect but Happy Family",
    "Great Friends",
    "Stable Job with 6 figure income", 
    "Business",
    "Wonders of the World", 
    "Beach House",
    "Comfortable Vehicle"
    ]

print(f"As I grow up I would like to achieve {bucket_list[0]}")
print(f"To my future family, I would like to have a {bucket_list[1]}")
print(f"As I am exploring my journey in life, I hope I would continue to meet and hang a lot of {bucket_list[2]}")
print(f"As I gradually move higher to my career, I would like to have a {bucket_list[3]}")
print(f"After all the exploration in Jobs, I would like to have my own {bucket_list[4]}")
print(f"That can sustain my exploration on the {bucket_list[5]}")
print(f"After the adventure I would like to own a {bucket_list[6]} that reminds me that I still have my own home")
print(f"Also atleast have my own {bucket_list[-1]}")

motorcycles = [
    "honda",
    "mitsubishi",
    "yamaha", 
    "suzuki"
]
print(motorcycles)

#Change a value on a specific index
motorcycles[2] = 'ahamay'
print(motorcycles)

#adding a data to an existing list 
motorcycles.append('ducati') #it will added to the end of the list
print(motorcycles)

#inserting an element into an existing list
motorcycles.insert(1, 'BMW') #It insert the value BMW to index 1 on the list
print(motorcycles)

#removing an item on the list
#   if you know the specific index, you can utilize this del statement: 
del motorcycles[1]
print(motorcycles)

#removing an item using the 'pop' method
popped_motorcycles = motorcycles.pop()
print(motorcycles) #the updated list of the data
print( f"The last motorcycle that I bought was {popped_motorcycles.title()}") #it prints the value that has been remove from the list

#popping an item from any Positions in a List
first_owned = motorcycles.pop(0)
print(f"The very first motorcycle that I owned was a {first_owned.title()}")

#diff of pop && del
#   use del when no longer want to use the value that you are going to remove
#   use pop when you still want to use the value 

#remove method
#if you don't know the position but know the value
tooExpensive = 'mitsubishi'
motorcycles.remove(tooExpensive)
print(f"{tooExpensive.title()} is too expensive for me.")

print(motorcycles)