class student:
    def __init__(self , name , grade): #constructor
        self.name = name
        self.grade = grade

    def display(self):
        print(f"The student {self.name} is in grade {self.grade} ")

s1 = student('Vishwak', 12)
s2 = student('Mohamed', 11)
s3 = student('Zayn', 10)

s1.display()#The student Vishwak is in grade 12
s2.display()#The student Mohamed is in grade 11
s3.display()#The student Zayn is in grade 10

# ===============================================================================================================
class employee:
    def __init__ (self , name , aadarNumber):
        self.name = name
        self.aadarNumber = aadarNumber

    def enterOffice(self):
        print(f"The person name {self.name} is entered with an aadhar number {self.aadarNumber}")

    def OpenBankAcc(self):
        print(f"The person named {self.name} is opened ad account using aadar number {self.aadarNumber}")

e1 = employee('vishwak','23345-2345-2345')

e1.enterOffice() #The person name vishwak is entered with an aadhar number 23345-2345-2345

e1.OpenBankAcc() #The person named vishwak is opened ad account using aadar number 23345-2345-2345
# ================================================================================================================

# without constructors
class MathTool:
    def square(self,n):
        result = n*n
        return result
    def cube(self,n):
        result = n*n*n
        return result

tool = MathTool()

print(tool.square(2))#4
print(tool.cube(3)) #27