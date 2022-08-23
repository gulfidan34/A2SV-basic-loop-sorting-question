def insertion_Sort(n,arr):
    
    key = arr[-1]
    i= n-1
    while i>0  and arr[i-1]>key:
        arr[i]=arr[i-1]
        print(*arr)
        i-=1
    arr[i]=key
    print(*arr)    
    
    
    
arr=[2,4,6,8,3]