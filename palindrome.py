def palindrome(n):
  revnum=0
  duplicate=n

  while n>0:
    ld=n%10
    revnum=(revnum*10)+ld
    n=n//10
  if dup==revnum:
    return True
  else:
    return False
def main():
  num=4884
  if palindrome(number):
    print("yes")
  else:
    print("no")

if __name__=="__main__":
  main()
