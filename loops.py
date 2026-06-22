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

#==============================================================================================================
num = int(input("Enter the number :"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print('* ' ,end= '')
    print("\n")
'''
* 

* * 

* * * 

* * * * 

* * * * * 
'''