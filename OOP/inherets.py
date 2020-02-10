class A:
    def feature1(self):
        print('feature one')

    def feature2(self):
        print('feature two')

# add all A data to B
class B(A):
    def feature3(self):
        print('feature three')

    def feature4(self):
        print('feature four')

class C(B):
    @staticmethod
    def feature5():
        print('feature five')

# add all A data to B
class D:
    def feature3(self):
        print('feature three')

    def feature4(self):
        print('feature four')

class E:
    @staticmethod
    def feature5():
        print('feature five')

class F(A,D,E):
    @staticmethod
    def feature5():
        print('feature five')

bClass = F()
bClass.feature3()
bClass.feature4()
bClass.feature2()
bClass.feature5()
