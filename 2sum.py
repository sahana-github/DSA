def two_sum(arr,t):
  hash={}
  for index,value in range(arr):
    remaining=t-arr[index]
    if remaining in hash:
      return[index,hash[remaining]]
    else:
      hash[value]=index
