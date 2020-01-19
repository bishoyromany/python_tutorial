from array import *

arr = array('i' , [10 , 50 , 15 , 20])

arr.reverse()

newArray = array(arr.typecode , (x*x for x in arr))

print(arr , arr.buffer_info() , arr[0] , newArray)

for val in range(len(arr)):
    print(arr[val])

vals = array('i' , [])

n = int(input('Enter Array Length'))

for i in range(n):
    x = int(input('Enter The Value'))
    vals.append(x)
print(vals)

v = int(input('Enter Search Value'))

x = 0
for i in vals:
    if v == i:
        print('Value WAs Found And Value is {0} And Index is {1}'.format(i , x))
        break
    x += 1

print(vals.index(v))