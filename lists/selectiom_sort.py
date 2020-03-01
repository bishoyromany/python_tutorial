def sort(arr):
    for i in range(len(arr) - 1):
        minpos = i 
        for j in range(i , len(arr)):
            if arr[j] < arr[minpos]:
                minpos = j
        print(arr)
        temp = arr[i]
        arr[i] = arr[minpos]
        arr[minpos] = temp
    return arr

arr = [70,20,40,50,10,2,1,0,50,40,30,4]

print(sort(arr))