goals = [
    'peace',
    'healthy'
    'job',
    'business',
    'beacehouse',
    'vehicle',
]

#sorting a list permanently
goals.sort()
print(goals)

#finding the length
print(len(goals))


goalPlaces = [
    'Petra',
    'Taj Mahal',
    'Christ the Redemeer',
    'Machu Picchu',
    'Chichen Itza',
    'Great Pyramid of Giza',
    'Great Wall of China',
    'Colosseum'
]

print(f"Original order: {goalPlaces}")

#sorting a list temporarily
sortedGoals = sorted(goalPlaces)
print(f"Sorted: {sortedGoals}")

reverseGoals = sorted(goalPlaces, reverse=True)
print(f"Reverse Sorted: {reverseGoals}")

print(f"Original Order: {goalPlaces}")
print(len(goalPlaces))

