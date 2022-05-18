# a=input("enter the string")
# b=a.replace('a','$')
# print(b)

#by using if else
# a=input("enter the string")
# b=a.replace('a','$')
# if b[0]=='$':
#     print("replace the first occurnce",b)
# else:
#     print("not replace")


#by using for loop
# a=input("enter the string")
# b=0

# # for x in a:
#     if x==a:
#         b=b+'$'
#     else:
#         b=b+'x'
# print("original",a)
# print("modified",b)


# by using function

def char(a):
    for x in a:
      if x=='a':
        b=b+'$'
b=0
a=input("enter the string")   
print(char(a))



 