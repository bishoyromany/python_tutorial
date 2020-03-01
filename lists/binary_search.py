def binary_search(arr , num):
    l = 0
    u = len(arr) - 1
    index = -1

    while l <= u:
        mid = (l + u) // 2

        if arr[mid] == num:
            index = mid 
            break
        else:
            if arr[mid] < num:
                l = mid+1
            else:
                u = mid-1           

    if index > -1:
        return index 
    else:
        return False            



arr = [1,2,10,20,50,70]

num = 70

searcher = binary_search(arr , num)

print(searcher)