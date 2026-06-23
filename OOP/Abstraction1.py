from abc import ABC , abstractmethod

class featurePlan(ABC):
    @abstractmethod
    def login(self): #abstract methods which must be implemented in the child class
        pass
    @abstractmethod
    def logout(self):
        pass

    def checkOut(self): #normal method which we can override if we want , not like abstract methods
        pass

class whatsApp(featurePlan):
    def login(self): # abstract method
        print("Loginned into whatsapp")

    def logout(self):
        print("Logged out")

    def checkOut(self):
        pass #not mandatry to implement this method


user = whatsApp()
user.login()
user.logout()



