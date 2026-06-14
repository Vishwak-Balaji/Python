name = "Vishwak balaji"

print(name.upper())  # change the string into upper case
print(name.lower()) # change the string into lower case
print(name.capitalize()) # make the first letter of the string to capital

mobile = "9988776654"
marked = mobile[:2]+"******"+mobile[-2:]
print(marked) # 99******54

song = "shape of you"
artist = "ed sheeran"

print(f"{song.title()} - {artist.title()}") #Shape Of You - Ed Sheeran - make first letter of the each word caps

location = "Coimbatore"
fixed_location = location.replace("Coimbatore","Chennai")
print(fixed_location) # replace function

message = "your uber booking i is : UA0134. please ride safe"
print(message.split(":")[1].split(".")[0].strip()) # print UA0134

promo_message = "The zomato100 is your copunn code"
if "zomato100" in promo_message:
    print("Offer applied")

feedback = "the ride was good and the driver is polite"
print("The position of the word polite is :",feedback.find("polite")) #36

