def linearSearch(arr , num):
    i = 0
    foundTimes = []

    for x in arr:
        i += 1
        if num == x:
            foundTimes.append(i)
            return i

    if len(foundTimes) > 0:
        return {
            'indexes' : foundTimes,
            'all' : i
        }
    
    return False


arr = [1,2,3,4,5,6,3]
n = 3 


searcher = linearSearch(arr , n)

if searcher:
    print(searcher)
else:
    print('Not Found')

