class Computer:

    # calls once class register like __construct
    def __init__(self , name , desc):
        self.name = name
        self.desc = desc
        self.config()

    def config(self):
        print(self.name)


com = Computer('MY PC' , 'This is my Own PC')