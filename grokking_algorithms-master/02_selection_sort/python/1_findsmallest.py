
# 寻找最小的数
def findsmallest(arr):
    item = arr[0]
    index=0
    for i in range(1,len(arr)):
        if arr[i]<item:
            item=arr[i]
            index=i
    return index,arr[index]

L=[2,10,3,5,3,7,9,8]
print(findsmallest(L))

def Sort(arr):
    
