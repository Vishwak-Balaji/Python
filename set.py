"""
Set → Unordered collection of unique values — uses { }
No duplicates → if you add the same value twice, it stores only once
Unordered → no index, you cannot access items using s[0]

"""
example = {1,2,3,4,5,5,4,3,1} #{1, 2, 3, 4, 5} no Duplicates allowed
#print(example)

uber_location = {"chennai","banglore","hydrabad"}
uber_location2 = {"delhi","pune","hydrabad"}

#Union in Sets
print(uber_location.union(uber_location2)) #Union combines all elements from both sets (no duplicates)
#{'hydrabad', 'pune', 'delhi', 'chennai', 'banglore'}

#Intersection in Sets
print(uber_location2.intersection(uber_location)) #Intersection gives only common elements from both sets
#{'hydrabad'}

#Difference in Sets
print(uber_location.difference(uber_location2)) #Difference gives elements that are in one set but NOT in the other
#{'chennai', 'banglore'}







