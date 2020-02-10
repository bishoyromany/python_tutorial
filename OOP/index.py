class Computer:
    # global for class and can't be changed out side
    numOfComputer = 10

    # calls once class register like __construct
    def __init__(self , name , desc):
        self.name = name
        self.desc = desc
        self.innerC = self.innerClass()
        self.config()

    def config(self):
        print(self.name , self.numOfComputer , self.returnClassVariable())

    @classmethod
    def returnClassVariable(cls):
        cls.numOfComputer = 'changed inside only'
        return cls.numOfComputer

    @staticmethod
    def staticMethod():
        print("this is static method")

    # register class inside class
    class innerClass: 
        def __init__(self):
            self.inner = 'this is my inner'
            print(self.inner)

com = Computer('MY PC' , 'This is my Own PC')
com.name = "edited"
com.numOfComputer = "edited"
instancee = com.innerC
instancee.inner = 'inner changed'
print(instancee.inner)

com.config()
com.staticMethod()

print(com.returnClassVariable())