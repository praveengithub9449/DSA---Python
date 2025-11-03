def BubbleSort(arr):
    n=len(arr)
 
    for i in range(n):
        for j in range(n-i-1):
            
            if arr[j] > arr [j+1] :
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print("i--",i,"j--",j,"j+1--",j+1,arr)
                flag=True
          
    return arr 





arr =[5,3,4,6,7,1]
print(BubbleSort(arr))