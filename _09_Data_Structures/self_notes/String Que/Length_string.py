#Direct method
a= input("enter the string:")
b=len(a)
print(b)

#by using if else method
a= input("enter the string:")
b=len(a)
print(b)
if b>1:
    print("lenght is greater than 1")
else:
    print("empty string")

#for loop
a=input("enter the string:")
c=0
for x in a:
    c+=1
print("lenght of string",c)

#by using Function
def lenght(a):
    c=0
    for x in a:
      c+=1
    return c
a=input("enter the string")
print(lenght(a))



