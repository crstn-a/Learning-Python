#reasons to store a set of num - 
#if in the game, you can track the position of each character
#track of player high scores 

#range() function - you can easily generate a series of num, generating not sorting
#range (start, stop)
for value in range(1, 5): #(start) begin the seq, #(stop), end the seq before this num
    print(value)

#off by 1 behaviour
#output - 1 2 3 4 

#if you want to store the generated series of your num
for listOfValue in list(range(1,5)):
    print(listOfValue)


#range (start, stop, step)
for evenNumbers in list(range(0, 11, 2)):
    print(evenNumbers)

# ** = exponents
squares = [] #empty list of squares
for value in range(1, 11):      #loop the var value through 1-10
    squares.append(value**2)    #current value is raised to the second power and added to the list of squares

print(squares) 
#output [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(min(squares))        #minimum of a list
max(squares)                #maximum of a list
sum(squares)                  #sum of a list

#list comprehension - generate this same list in just one line of code
circles = [value ** 2 for value in range(1,11)] 
print(circles)