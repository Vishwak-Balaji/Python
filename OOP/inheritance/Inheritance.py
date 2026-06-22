# single level inheritance
class dad:
    def house(self):
        print("Dad class")

class son(dad):
    def home(self):
        print("son class")

objDad = dad()
objSon = son()

objDad.house() #Dad class
objSon.home() #son class
objSon.house()#Dad class

#============================================================================================================
# over riding

class App1:
    def V1(self):
        print("version is just UI")
class App1_1(App1):
    def V2(self):
        print("Back end")
    def V1(self): # over rided the code from the parent class
        print("can place an order")

app = App1_1()
app.V1()
app.V2()
