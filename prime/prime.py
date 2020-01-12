from primeFunc import isPrime

# get prime
# x = [7 , 10 , 12 , 20 , 11]
# primeNumbers = []
# for y in x:
#     for i in range(2 , y):
#         if y % i == 0:
#             print('No Prime ' + str(y))
#             break
#     else:
#         primeNumbers.append(y)
#         print('Prime ' + str(y))
# print(primeNumbers)

x = range(1,101)

print(isPrime(x))