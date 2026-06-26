# variables and data type

a = "110"
b = "vishwak balaji T"
isTrue = True
c = 3.14
d ='x'

print(a , type(a)) # 10 <class 'str'>
print(b , type(b)) # vishwak <class 'str'>
print(isTrue , type(isTrue)) # True <class 'bool'>
print(c , type(c)) # 3.14 <class 'float'>
print(d , type(d)) # x <class 'str'>

#===============================================================================================

# variable scope - L E G B

    # L - local scope
def order():
     food = "rice"
     print(food)
order()

#print(food) # this will not work , coz the local variable is inside the function

    # E - Enclosed scope
def cart ():
    discount = 10
    def checkout():
        print("The discount is :",discount)
    checkout()
cart()

    # G - Global scope
user_id = "Vishwak_Venket" # global variable scope , which can be accessed from any where in the program

def homepage():
    print("welcome :",user_id)
def profile():
    print("welcome :",user_id)
homepage()
profile()

    #B - build in variable

print(__file__)
#========================================================================================================
# Type Casting
