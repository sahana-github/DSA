def bubblesort(arr):
  n=len(arr)
  for i in range(n-1,0,-1):
    for j in range(i):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr

arr=[64,9,89,12,100,2]
sorted=bubblesort(arr)
print(sorted)
      
