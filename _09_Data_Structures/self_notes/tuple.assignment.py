# Accessing elements of tuple:
# 	1. By using index:
# 	2. By using slice operator:

a=(1,2,3,4,5)
print(a[4])
print(a[1:4])
#---------------------------------------------------------
#Mathematical operators for tuple:
# + and * operators for tuple
tuple1=(1,2,3,4,5)
tuple2=(4,5,6,7,8)
print(tuple1+tuple2)


#------------------------------------------------------------------
# Important functions of Tuple:
# 	1. len(): 
tuple1=(1,2,3,4,5,5)
print("length",len(tuple1))

# 	2. count()
print("count",tuple1.count(5))

# 	3. index()
print("index",tuple1[0:2])
# 	4. sorted()
print("sorted",sorted(tuple1))

#min() and max() functions:
print("maximum",max(tuple1))
print("minimum",min(tuple1))
#------------------------------------------------------------------------------------
#Tuple Packing and Unpacking:
 #unpacking python tuple using *
 
# first and last will be assigned to x and z
# remaining will be assigned to y
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)
 
# print details
print(x)
print(y)
print(z)
 
# first and second will be assigned to x and y
# remaining will be assigned to z
x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50)
print(x)
print(y)
print(z)
#--------------------------------------------------------------------------
#Tuple Comprehension:
tuple=(1,2,3,4,5)
tuple2=(6,7,8,9)
print(tuple1+tuple2)
#---------------------------------------------------------------------------------------------------

# Write a Python program to check if a specified element presents in a tuple of tuples.

# 		Original list:
# 		(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# 		Check if White presenet in said tuple of tuples!
# 		True
# 		Check if White presenet in said tuple of tuples!
# 		True
# 		Check if Olive presenet in said tuple of tuples!
# 		False
def check_in_tuples(colors, c):
    result = any(c in tup for tup in colors)
    return result

colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)
print("Original list:")
print(colors)
c1 = 'White'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))
c1 = 'White'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))
c1 = 'Olive'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))
#----------------------------------------------------------------------------------------
# Write a Python program calculate the product, multiplying all the numbers of a given tuple.
# 		Original Tuple:
# 		(4, 3, 2, 2, -1, 18)
# 		Product - multiplying all the numbers of the said tuple: -864
# 		Original Tuple:
# 		(2, 4, 8, 8, 3, 2, 9)
# 		Product - multiplying all the numbers of the said tuple: 27648

tuple=(4, 3, 2, 2, -1, 18)
mul=1
for x in tuple:
    mul=mul*x   
print(mul)







