def getsinglenumber(arr):
    n=len(arr)
    for i in range(n):
        num=arr[i]
        cnt=0
    for j in range(n):
        
        if arr[j]==num:
            cnt+=1
      
    if cnt==1:
      return num
    return -1
  
      
    
def main():
  arr=[2,3,2,3,1]
  ans=getsinglenumber(arr)
  print("The Single element is :", ans)
main()
