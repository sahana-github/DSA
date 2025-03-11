def find_gcd(n1,n2):
  #initialise gcd to 1
  gcd=1
  # iterate from 1 to min of n1 and n2
  for i in range(1,min(n1,n2)+1):
    #check if its common factor
    if n1%i==0 and n2%i==0:
      #if yes then update to gcd variable
      gcd=i
    return gcd

if __name__==""_main__"":
  n1,n2=30,60

gcd=find_gcd(n1,n2)
print("gcd of" n1 "and" n2 "is", gcd)
