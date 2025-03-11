def selectionSort(arr):
  n=len(arr)
  for i in  range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
          min_index=j
          #Swap the found minimum element with the first element of the range
    arr[i],arr[mini_index]=arr[mini_index],arr[i]
  return arr

arr=[2,6,1,9,5]
sortedarr=selection_sort(arr)
print(sortedarr)
  
  
    
