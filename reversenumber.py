n=int(input("Enter Number:")

revnum=0

while n>0:
  # Extract the last digit of 'n' and store it in 'ld'
  ld=n%10
  # Multiply the current reverse numberby 10 and add the last digit.
  revnum=(revnum*10)+ld
  # Remove the last digit from 'n'
  n=n//10
print(revnum)
