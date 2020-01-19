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

r1,r2 = add_sub(10,20)
print(greet() , returnThis('wroking') , multipleThis(10) , selfParams(10) , r1 , r2 ,person(name="name" , age="age") ,
      sumIt(10 , 20 , 20 , 40 , 50 , 60 , 100) , fullPerson('Bishoy' , city="Cairo" , phone="1234" , country="egy" , age=18))