def findelement(arr):
  arr.sort()
  return arr[-1]
if __name__=="__main__":
  arr1=[2,4,5,10]
  print("The largest element in array is",findelement(arr))


#recurssive approch

# def findelement(arr,n):
#   max=arr[0]
#   for i in range(0,n):
#     if max<arr[i]:
#       max=arr[i]
#   return max
# if __name__=="__main__":
#   arr1=[2,8,90]
#   n=3
#   max=findelement(arr1,n)
#   print("largest element is",max)
      
    
  
  
