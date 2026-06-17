"""
Dictionary → stores data in key : value pairs — uses { }
Keys are unique → no duplicate keys allowed, values can repeat
Ordered → maintains insertion order (Python 3.7+)
Mutable → you can add, remove, and change values after creation
"""

trip={
    "Trip_id":"U1234",
    "Pickup":"Chennai Cenral",
    "Drop":"Airport",
    "fare":500.00,
    "Driver":"Raj",
    "Status":"Completed"
}

#lookup
print(trip["Pickup"]) #Chennai Cenral

#safe way to use
print(trip.get("Drop")) #Airport
print(trip.get("Airport")) #None

# to print the keys
print(trip.keys()) #dict_keys(['Trip_id', 'Pickup', 'Drop', 'fare', 'Driver', 'Status'])

# to print the values
print(trip.values()) #dict_values(['U1234', 'Chennai Cenral', 'Airport', 500.0, 'Raj', 'Completed'])

# to iterate
for key , value in trip.items():
    print(key ," : ",value) # prints all the key value pairs

#to add or update
# trip.update({"vehicle":"Car"}) # will add this in the dictionary , if it is already exist then it will update it
# print(trip)#{'Trip_id': 'U1234', 'Pickup': 'Chennai Cenral', 'Drop': 'Airport', 'fare': 500.0, 'Driver': 'Raj', 'Status': 'Completed', 'vehicle': 'Car'}
#
# trip.update({"vehicle":"Van"})# now car will be updated to van
# print(trip)  #{'Trip_id': 'U1234', 'Pickup': 'Chennai Cenral', 'Drop': 'Airport', 'fare': 500.0, 'Driver': 'Raj', 'Status': 'Completed', 'vehicle': 'Van'}


trip.update({"Pickup":["chennai","coimbatore"]})

print(trip['Pickup'][1])# coimbatore
