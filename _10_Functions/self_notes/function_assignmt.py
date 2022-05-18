#Write a function to take number as input and print its square value

def square(a):
    x=a*a
    return x
print("square",square(5))
#-----------------------------------------------------------
#Write a function to accept 2 numbers as input and return sum.

def sum(a,b):
    y=a+b
    return y
print("sum",sum(10,20))
#----------------------------------
#Write a function to check whether the given number is even or odd?


def number():
    z=3
    if z%2==0:
        print("even")
    else:
        print("odd")
number()
#-------------------------------------------------------
# #return sum,sub
# 	Output 
# 	The Sum is : 150 
# 	The Subtraction is : 50

#by using positional argument
def sum_sub_mul(a,b):
    l=a+b
    m=a-b
    n=a*b
    return l,m,n
print("(sum,sub,mul)",sum_sub_mul(5,4))
#by using default argument
def sum_sub_mul(a,b=10):
    l=a+b
    m=a-b
    n=a*b
    return l,m,n
print("(sum,sub,mul)",sum_sub_mul(5))
#by using keyword argument
def sum_sub_mul(a,b):
    l=a+b
    m=a-b
    n=a*b
    return l,m,n
print("(sum,sub,mul)",sum_sub_mul(a=5,b=4))
#by using varible length keyword
def sum_sub_mul(a,*b):
    l=a+b
    m=a-b
    n=a*b
    return l,m,n
print("(sum,sub,mul)",sum_sub_mul(5,4,10))
#----------------------------------------------------------------------------------------------------------
#Table of the given number

def Table():
    n=3
    for i in range(1,11):
        print(n,'x',i,'=',n*i)
Table()
#-----------------------------------------------------------------------------------
#sum all the numbers in a list,set,tuple


def list(a):
    total=0
    total2=1
    for x in a:
        total=total+x
        total2=total2*x
    return total,total2
a=[1,2,3,4,5,6,7]
ans=list(a)
print("sum and mulitplication of all number in list is:",ans)

def set(a):
    total=0
    total2=1
    for x in a:
        total=total+x
        total2=total2*x
    return total,total2
a={1,2,3,4,5,6,7}
ans=set(a)
print("sum and mulitplication of all number in set is:",ans)

def tuple(a):
    total=0
    total2=1
    for x in a:
        total=total+x
        total2=total2*x
    return total,total2
a=[1,2,3,4,5,6,7]
ans=tuple(a)
print("sum and mulitplication of all number in tuple is:",ans)

#---------------------------------------------------------------------------------------------------------------------------------
#Accepts a string and calculate the number of upper-case letters and lower case  letters

a=input("enter the string")
def low_upp(a):
    c1=0
    c2=0
    for x in a:
        if (x.isupper()):
            c1+=1
        elif (x.islower()):
            c2+=1
    print("upper count are:",c1)
    print("lower count are:",c2)

low_upp(a)

#-------------------------------------------------------------------------------------------------------------------------
#Take a list and return a new list with unique elements of the first list.
 
 
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 

#-----------------------------------------------------------------------------------------------------------------------------
#Print given Pascal's triangle

n = 5
for i in range(n):
    for j in range(n-i+1):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    # for new line
    print()

#------------------------------------------------------------------------------------------------------------------------------------
#Function to check whether a string is a palindrome or not

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "radar"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

#----------------------------------------------------------------------------------------------------------------------------
#check whether a number is in a given range

def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)


