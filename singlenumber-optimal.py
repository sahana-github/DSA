def getsinglenumber(arr):
  xorr=0
  for i in arr:
    xorr^=i
  return xorr

def main():
  arr=[2,3,2,3,1]
  ans=getsinglenumber(arr)
  print("The Single Element is",ans)
  main()
