# check prime using function
def isPrime(nums):
    primeNumbers = []
    notPrimeNumbers = []
    for y in nums:
        for i in range(2,y):
            if y % i == 0:
                notPrimeNumbers.append(y)
                break
        else:
            primeNumbers.append(y)
    return {'primeNumbers' : primeNumbers , 'notPrimeNumbers' : notPrimeNumbers}
