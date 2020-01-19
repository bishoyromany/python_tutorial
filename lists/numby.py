from numpy import *

arr = array([1 , 2 , 3 , 4] , int)
# get type
print(arr , arr.dtype)
# float values
lins = linspace(0 , 15 , 16)
print(lins)
# arange
rang = arange(0 , 100 , 5)
print(rang)
# float values
lins = logspace(0 , 40 , 5)
print(lins)
# ones and zeros
ones = ones(10 , int)
zeros = zeros(10 , int)
print(ones , zeros)

# coping
arr1 = array([10 , 20 , 30 , 40])
arr2 = arr1.copy()

arr = arr+arr2
arr = arr+5
print(arr1 , arr2 , id(arr2) , id(arr1))

print(sin(arr) , cos(arr) , log(arr) , sum(arr) , max(arr))

# matrix
bigArray = array([
    [1,2,3,4],
    [5,6,7,8]
])
# 1 dim
bigArray2 = bigArray.flatten()
# multiple dim
bigArray3 = bigArray.reshape(bigArray.shape)

print(bigArray , bigArray.dtype , bigArray.ndim , bigArray.shape , bigArray.size)
print(bigArray2)
print(bigArray3)

# matrix
m = matrix(bigArray)
m1 = matrix('1 2 3 4 ; 5 6 7 8')
m2 = matrix('1 2 3 4 ; 5 6 7 8')
print('')
print(m)
print(m2)
print(diagonal(m2) , m.min() , m.max())