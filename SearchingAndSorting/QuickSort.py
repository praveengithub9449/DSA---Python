def QuickSort(arr):
    if len(arr)<=1:
        return arr

    pvoit=arr[-1]
    print (pvoit)

    left=[x for x in arr[:-1] if x <= pvoit]
    print(left)
    right = [x for x in arr[:-1] if x > pvoit]
    print(right)
  
    return QuickSort(left) + [pvoit] + QuickSort(right)

arr=[5,4,7,8,3,2]
print(QuickSort(arr))