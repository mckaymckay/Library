# binary search


def binary_search(list, num):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        item = list[mid]
        if item < num:
            low = mid + 1
        elif (item > num):
            high = mid - 1
        else:
            return mid
    return None


print(binary_search([1, 2, 3, 4, 5], 1))
print('************')
print(binary_search([1, 2, 3, 4, 5], 6))
