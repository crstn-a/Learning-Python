castAttackOnTitan = [
    'Eren',
    'Mikasa',
    'Armhi',
    'Thomas',
    'Sasha'
]

#print("#Change into alphabetical order")  #-- and cannot revert to the original order
#castAttackOnTitan.sort()
#print(castAttackOnTitan)

#print("#Sort into reverse-alphabetical order")
#castAttackOnTitan.sort(reverse=True)
#print(castAttackOnTitan)

print("#Sorting a list temporarily")
#Sorted() func display the list in particular order, but doesn't affect the actual order original list.
print (f"The original list: {castAttackOnTitan}")

TempSort = sorted(castAttackOnTitan)
print(f"The temporary sorted list: {TempSort}")

print(f"Here is the original list again: {castAttackOnTitan}")