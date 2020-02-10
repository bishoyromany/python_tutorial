class A:
    def __init__(self):
        print('INIT A')

    def feature1(self):
        print('feature one')

    def feature2(self):
        print('feature two')

# add all A data to B / if same function exist in both, then B will work
class B(A):
    def __init__(self):
        # run a specific A method
        super().__init__()
        print('INIT B')

    def feature3(self):
        print('feature three')

    def feature4(self):
        print('feature four')

bClass = B()
bClass.feature3()
bClass.feature4()
bClass.feature2()


# add option
class addClass:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2 
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = addClass(m1 , m2)
        return s3

    def __gt__(self, other):
        o = other.m1 + other.m2
        s = self.m1 + self.m2 
        if s > o:
            return True
        else:
            return False
    def __str__(self):
        return "M1 is : {} & M2 is : {}".format(self.m1 , self.m2)

    def sum(self, a , b , c=0):
        return a + b + c



s1 = addClass(10 , 71)
s2 = addClass(40 , 40)

s3 = s1 + s2 

print(s3.m1 , s1 > s2 , s1 , s1.sum(1,2))