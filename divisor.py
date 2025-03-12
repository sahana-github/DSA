def divisor(n):
  arr=[]
  for i in range(1,n+1):
    if n%i==0:
      arr.append(i)
  return arr

def main():
  num=12
  divi=divisor(num)
  print(divi)
main()
