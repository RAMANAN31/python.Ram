"""#functions 
def greet(x,y):
    print('hi')
    print('welcome')
    return (x*x)*y
greet(4,y=5)#keyword argument
def get_greeting(name):
     return 'hi'+name
m1=get_greeting("ram")
file=open("file1.txt","a+")#saving in a file
file.write(m1)
print(m1)
#for lists to find product of numbers
def mult(*number):
    total=1
    for num in number:
        total*=num#total=total*num
    return total
print(mult(2,2,3))
#**args,using** will allow us to give multiple key 
#value pairs and it will be converted into a dictionary.
def user(**user):
    print(user)
    global message
    message='c'
user(id=1,name="john",age=22)
print(message)"""
#fizzbuzz algorithm
def fizzbuzz(input):
    if input %3==0:
        return "Fizz"
    if input %5==0:
        return "Buzz"
    if (input %3==0)and(input %5==0):
        return "FizzBuzz"
    return input
        
print(fizzbuzz(15))
