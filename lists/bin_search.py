def bin_search(arr , num):
    up = len(arr) - 1 
    low = 0 
    index = -1

    while low <= up:
        mid = (low + up) // 2 
        if arr[mid] == num:
            index = mid 
            break 
        else: 
            if arr[mid] < num:
                low = mid + 1 
            else: 
                up = mid - 1

    if index > -1:
        return index 
    else:
        return False 

arr = [1,10,50,100,110]
num = 110 

print(bin_search(arr , num))

