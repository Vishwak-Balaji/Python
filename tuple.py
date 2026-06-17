"""
List → Mutable (can add, remove, change items) — uses [ ]
Tuple → Immutable (cannot change once created) — uses ( )
"""

trip_summery = ("rapido","Coimbatore","railway station",500.00,"completed")

# to find the index value
# print(trip_summery[2])# railway station

# to count the value
# print(trip_summery.count("rapido"))# 1

# Not methods, but built-in functions that work on tuples

n = (9,7,5,1,4)

min = min(n)
length = len(n)
maxx = max(n)
sum = sum(n)
sorted = sorted(n)
list = list(n)

print(min) #1
print(length) #5
print(maxx) #9
print(sum) #26
print(sorted) #[1, 4, 5, 7, 9]
print(list) # [9, 7, 5, 1, 4] this is a list not Tuple
print(type(list)) #<class 'list'>


# allowed to modify coz it is a tuple
list.append(6)
print(list) #[9, 7, 5, 1, 4, 6]



