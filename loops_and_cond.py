n= input(" enter a numbr= ")#create a variable named n and assign it to the user's response. Note that the function input always returns the user's response to the prompt as a string. So, n is a string.
n=int(n) #converted to integer
if n<5:
  print('less than 5:')
else
  print('more than 5:')
elif n==5 and n!=0  #The control flows to another part of the program.Correct conditional statement controls the flow of a program by testing whether a specific condition is met.
  print('equal')

for i in range(4)#range(start,stop,step)
  print (i) # When a starting number is not provided, range defaults to starting with zero. When a step size is not provided, range defaults to using a step size of one
# 0
# 1
# 2
# 3

#Running a code block zero, one, or many times is possible with iteration
for i in  range(1,8,2)
vowels=['a','e','i','o']
for v in vowels
print(v)
# using a built in len() function which gets the length 
#while loop
#hen you iterate over a sequence using a While Loop, the length of the sequence determines the number of repetitions. 
#The length of the list vowels, which is given by Len vowels is five. So five repetitions will take place, unlike a For Loop, a While Loop needs the Loop variable to be created and initialized beforehand. And note that to initialize a variable, means to give the variable an initial value. So I create a variable named I and initialized it to zero. 
#And I served as my Loop variable

vowels=['a','e','i','o']
i=0
while i<len(vowels)
  print(vowels(i))
  i++
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
The syntax for a nested while loop statement in Python programming language is as follows −

while expression:
   while expression:
      statement(s)
   statement(s)
A final note on loop nesting is that you can put any type of loop inside of any other type of loop. For example a for loop can be inside a while loop or vice versa.

Example
The following program uses a nested for loop to find the prime numbers from 2 to 100 −

 Live Demo
#!/usr/bin/python

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1

print "Good bye!"
