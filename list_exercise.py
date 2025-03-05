#Guest List
#If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

guestList = [
    'Rose',
    'Elsa',
    'Alliah'
]
print(guestList)
print(f"I would like to have a Dinner with {guestList[0]}")
print(f"There's no way I can have a Dinner with {guestList[1]}")
print(f"Hello, Can I have Dinner with you, {guestList[2]}?")

#1 guest can't make into dinner 
guestList[1] = 'Ed Sheeran'
print(guestList)

#modify- replace the name of the new guest - print a second set of invitation
print(f"I would like to have a Dinner with {guestList[0]}")
print(f"{guestList[1]} just want to join a Dinner Party, so I added him.")
print(f"{guestList[2]} dinner with me?")

#You've just found a bigger table 
#Inform the participants 
#use insert () to add one new guest to the beginning of the list
#use insert () to add one new guest to the middle of the list
#use append () to add one new guest to  of the list

guestList.insert(0, 'Elsa')
guestList.insert(2, 'Jack')
guestList.append('Noa')

print(guestList)

print(f"{guestList[0]} just change her mind, and now she wants to go!")
print(f"{guestList[1]} just accepted the invitation.")
print(f"I don't with {guestList[2]}.")
print(f"{guestList[3]} suggest that he want to sing to the Dinner Party, yey!")
print(f"How about {guestList[4]} and {guestList[5]}?")

#table won't arrive in time- now you just have 2 space for only two guest.
print(f"Sorry the Dinner Party will reschedule {guestList.pop()}")
print(f"Sorry, how about next time {guestList.pop()}?")
print(f"Sorry, would reschedule your singing next time {guestList.pop().title()}")
print(f"Sorry the table is sinking {guestList.pop().title()} :(")

print(guestList)

print(f"How about we have mini tea {guestList[0]} and {guestList[1]}?")

#del the last two names in my list
del guestList[1]
del guestList[0]
print(guestList)


len(guestList)