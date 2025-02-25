def is_sorted(arr):  
    
    ascending=True
    descending=True
    for i in range(len(arr)-1):
        
            if arr[i]>arr[i+1]:
                ascending= False
            if arr[i]<arr[i+1]:
                descending=False
    return ascending or descending
            
    return True
arr1=[1,2,3,4,5]
arr2=[5,4,3,2,1]
arr3=[2,9,2,9,2]

print(f"{arr1} is sorted in either direction:{is_sorted(arr1)}")
print(f"{arr2} is sorted in either direction:{is_sorted(arr2)}")
print(f"{arr3} is sorted in either direction:{is_sorted(arr3)}")
