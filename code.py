# Prime-number
#user  have to enter a positive integer range [A, B] and system will find out the status (Prime or composite) of each number available in the given range. At the end print the count also.

"""In this project you have to enter a positive integer range [A, B] and system will find out the status (Prime or composite) of each number available in the given range. At the end print the count also.
Note: Make use of efficient approach to check prime status of the number.
For example:
Range is (7,10) 
Then the status of each number in the range is:
7 is prime
8 is composite or not prime
9 is composite
10 is composite
Count: 1 prime and 3 composite numbers in the range.
(Student is free to decide the input and output layout for this mini project)
"""
def prime(x):
    c=1
    for i in range(3,x):
        if x%i==0:
            c=0
            break
    return c
#main
a=int(input("enter the starting range: "))
b=int(input("enter the ending range: "))
c,p=0,0
for i in range(a,b+1):
    if i<=0:
        print("please enter positive number greater then 0 ")
    elif i==1:
        print("1 is neither prime nor composite its a special number")
    else:
        t=prime(i)
        if t==0:
            print(i,"is a composite number")
            c+=1
        elif t==1:
            print(i,"is a prime number")
            p+=1
print("there are ",p,"prime number and  there are",c,"composite in the range",a,"and",b)


        
            
            
