#LOOPS

# basic for loop example
name = ['vishwak','Ramya','gokul','krishna']

for i in name:
    print(i.upper()) # print each names in upper case.

# while loop example

correct_password = "5342"
enter_password = ''

while correct_password != enter_password:
    enter_password = input("Enter the Password :")

print("Access granted...!")