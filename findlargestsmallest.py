def findlargest(arr):
    largest=arr[0]
    smallest=arr[0]
    
    for num in arr:
        if num>largest:
            largest=num
        if num<smallest:
            smallest=num
    return largest, smallest
arr=[1,4,90,8,0]
largest,smallest=findlargest(arr)
print("largest element in array",largest)
print("smallest element in array",smallest)
