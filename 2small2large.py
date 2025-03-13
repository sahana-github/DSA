def secondsmallest(arr,n):
  if(n<2):
    return -1
    # Initialize smallest & second smallest to infinity (a large number)
  small=float('inf')
  second_small=float('inf')
  for i in range(n):
    # If the current element is smaller than 'small', update both 'small' and 'second_small'
    if (arr[i]<small):
      second_small=small # The previous smallest becomes the second smallest
      small=arr[i] # Update 'small' to the new smallest element
       # If the current element is greater than 'small' but smaller than 'second_small',
    # update 'second_small' (ensuring it's not equal to 'small')
    elif (arr[i] < second_small and arr[i]!=small):
      second_small=arr[i]
  return second_small

def secondlarge(arr,n):
  if(n<2):
    return -1
     # Initialize largest & second largest to negative infinity (a very small number)
    large=float('-inf')
    second_large=float('-inf')
    for i in range(n):
      if(arr[i]>large):
        second_large=large
        large=arr[i]
      elif(arr[i]>second_large and arr[i]!=large):
        second_large=arr[i]
    return second_large

if __name__=="__main__":
  arr=[1,2,4,7,7,5]
  n=len(arr)
  ss=secondsmallest(arr,n)
  ll=secondlarge(arr,n)
  print("Second smallest is",ss)
  print("Second largest is", ll)

main()
      
