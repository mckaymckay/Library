def binary_search(list, num):
    low = 0
    high = len(list) - 1
   
    while low<=high:
        mid = (low + high) // 2
        if (list[mid] == num):
            return mid
        elif (list[mid] < num):
            low = mid + 1
        else:
            high = mid - 1
    return None

L1 = [2,34,5,36,54,68]
print(binary_search(L1,3))
print(binary_search(L1,2))
