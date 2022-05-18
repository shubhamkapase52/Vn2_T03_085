total = 1
 
# creating a list
a = [11, 5, 17, 18, 23]
 
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(a)):
    total = total * a[ele]
 
# printing total value
print("multiple of all elements in given list: ", total)

# by using function
def sum():
    total=1
    a = [11, 5, 17, 18, 23]
    for ele in range(0, len(a)):
       total = total * a[ele]
    print("multiple of all elements in given list: ", total)
sum()
 