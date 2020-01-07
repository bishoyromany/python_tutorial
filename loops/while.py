# while loop
x = 0
y = [
    'one' , 'tow' , 'three' , 'four' , 'five' ,
    'six' , 'seven' , 'eight' , 'nine' , 'ten'
]
while x < 10:
    print(y[x])
    x += 1
i = 0
y = 0
persons = ['Mina' , 'Joosh' , 'Archer' , 'Kingo']
while i < 5:
    print('Hello' , end="")
    while y < 4:
        # last one
        if y == 4-1:
            print(' And '+persons[y])
        else:
            if y == 0:
                print(' '+persons[y] , end="")
            else:
                print(' , '+persons[y] , end="")
        y += 1
    i+=1
    y = 0
