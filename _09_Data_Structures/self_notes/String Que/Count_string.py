# #By using method
# a=input("enter the string")
# b=a.count('a')
# print(b)

#by using if else method
# a=input("enter the string")
# b=a.count('a')
# print(b)
# if b>1:
#     print("counted")
# else:
#     print("Not repeated")

# by for loop
# a=input("enter the string")
# c=0
# for x in a:
#     if x=='a':
#         c+=1
# print(c)

#By using Function
def count(a):
    c=0
    for x in a:
        if x=='a':
          c+=1
    return c
a=input("enter the string")
print(count(a))

    





