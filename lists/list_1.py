# [1] -> Normal List
x = [1,2,3,4,5]

# can be read like strings
print(x[1:])

# can add multiple lists together
list1 = [1,2,3,4,5]
list2 = ['he' , 'she' , 'we' , 'you' , 'they']
list3 = [list1 , list2]
print(list3)

# [1] -> Lists Functions

# [1] inset(index , 'value') -> insert values to data
list3.insert(2 , 'New')
print(list3)
# [2] remove(value) -> removes value
list3.remove('New')
print(list3)
# [3] pop(index) -> removes value / without index it gonna remove last value
list3.pop(1)
print(list3)
# [4] del list[index] -> removes value
del list3[0]
print(list3)
# [5] extend(list) -> add multiple value
list3.extend(['Val1' , 2 , 3])
print(list3)

# Min , Max m sum and sorting For Numbers List
nums = [1,2,3,4,5,0]
print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)