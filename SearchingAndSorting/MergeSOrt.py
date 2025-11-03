def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j <len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    result.extend(left[i:])
    result.extend(right[j:])
    return result



def MergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=MergeSort(arr[:mid])
    right=MergeSort(arr[mid:])
    print(left,right)
    return merge(left,right)


arr =[7,23,5,6,9,10]
print(MergeSort(arr))