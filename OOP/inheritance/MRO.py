
# MRO - method resolution order
#this solves the diamond problem in the multiple inheritance

class Parent1 :
    def method_1(self):
        print("Iam in parent 1 class in method_1 ")
class Parent2 :
    def method_1(self):
        print("Iam in parent 2 class in method_2 ")
class Child(Parent1 , Parent2):
    pass

obj = Child()
obj.method_1()

'''
Child inherits from both Parent1 and Parent2, and both classes contain a method named method_1().
Python uses MRO (Method Resolution Order) to decide where to look for a method: Child → Parent1 → Parent2 → object.
Since Parent1 comes before Parent2 in the MRO and has method_1(), obj.method_1() executes Parent1's method and prints:'''
