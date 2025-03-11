def armstrong(n):
  #get the len of number
  k=len(n)
  #create sum to store sum of its power of number
  sum=0
  #create a copy of number
  copy=n
  while copy>0:
    #extract each digit
    ld=copy%10
    #add it to sum and digit raised to power of k
    sum+=ld**k
    #remove last digit of number
    copy=copy//10
    #check if sum is equal to number
  return sum==num

def main():
  number=153
  if armstrong(n):
    print(n, "Armstrong number")
  else:
    print(n, "is not Armstrong number")
if __name__== "__main__":
    main()
    
