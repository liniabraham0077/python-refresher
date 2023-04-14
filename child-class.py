from parent import Calculator

class Child(Calculator):

    def __init__(self):
        Calculator.__init__(self,4,4)
    def getData(self):
        return self.add();

childObj = Child()
print(childObj.getData())