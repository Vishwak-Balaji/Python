# basics (if, elif , else)

# grade =95
#
# if grade>=90 and grade <=100:
#     print("Grade - A+")
# elif grade >= 80 and grade <90:
#     print("Grade - A")
# elif grade >= 60 and grade <80:
#     print("Grade - B")
# elif grade >= 50 and grade <60:
#     print("Grade - C")
# else:
#     print("Fail")

#==========================================================================================================

# nested if

age = int(input("Enter your age :"))
if(age >=18):
    haveLisence = input("Have lisence ? (yes/no) :").lower()
if(age >= 18):
    if(haveLisence == "yes"):
        print("Yes you can rent a bike")
    else:
        print("you can't rent a bike")
else:
    print("you are not eligible to rent a bike")