def check(nums):
  count=0
  for i in range(len(nums)):
    if nums[i]<nums[i-1]:
      count+=1
  return count<=1  # A rotated sorted array should have at most one break
