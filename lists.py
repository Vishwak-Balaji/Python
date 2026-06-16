playlist = ['red cardu','shape of you','beliver','perfect']

# to add a new song
playlist.append('naa ready')
#print(playlist)

# to insert in a particular index
playlist.insert(1,'adavadi')
# print(playlist)

# to remove
playlist.remove("shape of you")
# print(playlist)

# to remove the last value
playlist.pop()
# print(playlist)

# to reverese a list
playlist.reverse()
# print(playlist)

# using slice print first few values
print(playlist[0:2])

# using slice print last few values
print(playlist[-2:])

# iterate the list:
menu = ['idly','sambar','vadai','dosa','pizza']
for i in menu:
    print(i)

# to check a particular values in the list
random = [1,2.2,3.00,'vishwak']
if "vishwak" in random:
    print("yes")

# print with index :
recent_location = ['coimbatore','chennai','banglore','pune']

for i, location in enumerate(recent_location):
    print(f"location {i} = {location}")



