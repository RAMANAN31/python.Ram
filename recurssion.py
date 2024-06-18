def factorial(n):
  """Return the factioral of integer n."""
if n==1:
  return 1;
else:
  return n*factorial(n-1)

def sum_digits(n)
  """sum of digits"""
 if n<10:
   return n
 else:
   before_last=n//10 #floor division
   last=n%10
   return sum_digits(before_last)+last
   # Note that integer division, denoted by the double forward slash, expresses the result of the division as 
#an integer by cutting off decimal points and everything after the decimal points if the original result is not an integer. 
#So you can get all the digits before the last digit of N by doing N double forward slash 10.




