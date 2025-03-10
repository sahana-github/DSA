def countdigits(n):
  # Initialize a counter variable'cnt' to store the count of digits.
  cnt=0
  # While loop iterates until 'n' becomes 0 (no more digits left).
  while n>0:
    # Increment the counter for each digit encountered.
    cnt=cnt+1
    # Divide 'n' by 10 to remove the last digit.
    n=n//10
  return cnt

if __name__ == "__main__":
  n=12345
  print("Number",n)
  digits=countdigits(n)
  print("number of digits are:", digits)
