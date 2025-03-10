import math
# Calculate the count of digits in 'n' using logarithmic operation log10(n) + 1.
def countdigits(n):
  cnt=int(math.log10(n)+1)
    # Expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
    # Return the count of digits in 'n'.
return cnt

if __name__=="__main__":
  n=12345
  print("Number",n)
  digits=countdigits(n)
  print("Number of digits are",digits)
