def find_gcd(n1,n2):
 
  while n1>0 and n2>0:
    if n1>n2:
      n1=n1%n2
    else:
      n2=n2%n1
    if n1==0:
      return n2
    else:
      return n1

def main():
  n1=20
  n2=15

  gcd=find_gcd(n1,n2)
  print(f"GCD of {n1} and {n2} is: {gcd}")
    
    
