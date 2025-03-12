def two_sum(n,arr,t):
  for i in range(n):
    for j in range(i+1,n):
      if arr[i]+arr[j]==t:
        return "YES"
      
    return "NO"
def main():
  n=5
  arr=[2,6,5,8,11]
  t=14
  ans=two_sum(n,arr,t)
  print(ans)
 main()
