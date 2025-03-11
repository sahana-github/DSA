def gcd(n1,n2):
  gcd=1
  for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
      gcd=i
    return gcd

if __name__==""_main__"":
  n1,n2=30,60

gcd=find_gcd(n1,n2)
print("gcd of" n1 "and" n2 "is", gcd)
