# Functions

def greet():
    print("Hello world")
greet()

#1 with arguements
def add(a,b):
    print(a+b)
add(1,22) #23

#2 with return

def add(a,b):
    return a+b
result = add(2,3)
print(result)

# with *args :
def add(*args):
    total = 0
    for i in args:
        total+=i
    return total
result = add(1,2,3,4,5)
print(result)

# functions for key value pairs (**kwargs)

def create_profile(**kwargs):
    print("User Values :")
    for key , value in kwargs.items():
        print(f"{key} : {value}")

create_profile(name="vishwak" , age= 22 , jobDescription = "software engineer")

