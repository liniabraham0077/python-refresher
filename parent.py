class Calculator:

    # constructor
    def __init__(self):
        print('constructor called automatically!!!')
    def __init__(self,a,b):
        print('constructor with args!!!')
        self.one=a
        self.two=b

#class variable
    num1=10
    num2=20

    def add(self):
        return self.one+self.two+ Calculator.num1
    def helloworld(self):
        print("beautiful world!")

# create object - new is not required
# obj = Calculator()

obj = Calculator(10,20)
obj.helloworld()
print(obj.num1)
print(obj.add())
