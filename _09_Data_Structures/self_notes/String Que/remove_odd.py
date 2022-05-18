# a=input("enter the string")
# b=""
# for x in range(len(a)):
#     if x%2==0:
#         b=b+a[x]
# print("after removing odd index value in a string:",b)

def remove_odd():
    a=input("enter the string")
    b=""
    for x in range(len(a)):
      if x%2==0:
         b=b+a[x]
    print("after removing odd index value in a string:",b)
remove_odd()
