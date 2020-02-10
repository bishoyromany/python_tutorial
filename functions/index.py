# empty function
def greet():
    pass

# can return
def returnThis(text):
    return text

# multiple
def multipleThis(num):
    return int(num) * int(num)

# self added params
def selfParams(m , num = 20):
    return int(num) * int(m)

# multiple reuturn
def add_sub(x , y):
    c = x + y
    b = x - y
    return c,b
# name arg
def person(name , age):
    return {'name' : name , 'age' : age}
# variable args
def sumIt(a , *b):
    c = 0
    for x in b:
        c += int(x)

    return c * int(a)

# kwargs args
def fullPerson(name , **data):
    forData = {'name' : name}
    for v,k in data.items():
        forData[k] = v
    return forData

# global vars
b = 10
def bIsGloblaHere():
    # global b
    # or
    b = 10
    x = globals()['b']
    x = 20
    return [b , x]

# list
lst = [5,10,30,40,100,52,60 , 75]
def oddEven(lis):
    odd = 0
    even = 0
    for i in lis:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return {'odd' : odd , 'even' : even}


def fib(n):
    nums = []
    for i in range(n):
        nums.append(i)
        if i < 2:
            nums[i] = i
        else:
            nums[i] = nums[i - 1] + nums[i - 2]
    return nums


def fact(n):
    if(n == 0):
        return 1
    return n * fact(n - 1)

square = lambda a,b : int(a + b) + int(a*b) * int(a + b) + int(a*b)


r1,r2 = add_sub(10,20)
print(greet() , returnThis('wroking') , multipleThis(10) , selfParams(10) , r1 , r2 ,person(name="name" , age="age") ,
      sumIt(10 , 20 , 20 , 40 , 50 , 60 , 100) , fullPerson('Bishoy' , city="Cairo" , phone="1234" , country="egy" , age=18) ,
      bIsGloblaHere() , b , oddEven(lst) , fib(20) , fact(5) , square(5,5))
