from functools import reduce

arr = [0,1,2,3,4,5,6,7,8,9]

evans = list(filter(lambda a : a%2 == 0 , arr))

doubles = list(map(lambda a : a * 2 , evans))

allData = reduce(lambda a,b: a+b , doubles)

print("Evans are {evans} And Doubles Are {doubles} And All is {all}".format(evans = evans, doubles = doubles, all = allData) , end="")