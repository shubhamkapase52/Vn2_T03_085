# Traversing the elements of List:
# By using while loop:
i=0
sum=0
while i<10:
    num=5
    sum = sum + num
    i+=1
print("sum",sum)
#------------------------------------------------------------------------
#  By using for loop:

cheeses = ["Gouda", "Swiss", "Provolone", "Cheddar"]
for cheese in cheeses:
    print(cheese)
#-------------------------------------------------------------------------
 #To display only even numbers:
list=[1,2,3,4,5,6,7,8,9,10]
even=[]
for x in list:
    if x%2==0:
        even.append(x)
print("even",even)
#----------------------------------------------------------------------

#To display elements by index wise(-Ve, +ve):
list=[1,2,3,4,5,6,7,8]
b=list[0:9]
c=list[::-1]
print(b)
print(c)

#-------------------------------------------------------------------------

# I. To get information about list:

# 1. len(): Return the number of element in the list
# 2. count():return the number of the times given element in the list
# 3. index() function:return the index of given element

#---------------------------------------------------------------------
# . Manipulating elements of List:
# 1. append() function:
list=[1,2,3,4,5,6,7,8]
list.append(10)
print(list)
# 2. insert() function:
list=[1,2,3,4,6,7,8]
list.insert(4, 5)
# Differences between append() and insert()
#  append():  adding the single element at end of list
#  insert():  adding the elment at specific posotion
# 3. extend() function:
list=[1,2,3,4,5,6,7,8]
list2=[9,10,11,12,13]
list.extend(list2)
print("extend",list)
# 4. remove() function:
list=[1,2,3,4,5,6,7,8]
list.remove(5)
print("remove",list)
# 5. pop() function:
list=[1,2,3,4,5,6,7,8]
list.pop(3)
print("pop",list)


# Differences between remove() and pop()
#remove(): remove the element from the list
#pop(): remove the element at given postion

#---------------------------------------------------------------------------------
# III. Ordering elements of List:
# 1. reverse():
list=[1,2,3,4,5,6,7,8]
list.reverse()
print("reverse",list)

# 2. sort() function:
list=[1,2,3,4,5,6,7,8]
list.sort()
print("sort",list)
#--------------------------------------------------------------------------------

# 1. By using slice operator(using = operater)
# 2. By using copy() function:
#shallow copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

#deeep Copy
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

#--------------------------------------------------------------------------------------------------

n=[[10,20,30],[40,50,60],[70,80,90]]
for x in n:
    print(x)

for x in n:
    for i in x:
       print(i,end=" ")
    print()

#----------------------------------------------------------------------------------------------------

# List Comprehensions:
words="the quick brown fox jumps over the lazy dog"
a=words.split(" ")
print([a])

for x in a:
    k=len(x)
    print([x,k])

#-----------------------------------------------------------------------------------------
# Write a Python program to convert a given list of tuples to a list of lists.
# Original list of tuples:

# [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of lists:
# [[1, 2], [2, 3], [3, 4]]

a=[(1, 2), (2, 3), (3, 4)]
for x in a:
    print([x])

#-------------------------------------------------------------------------------
#find common element from list
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")
          
  
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)
#-------------------------------------------------------------------------------------
#Replace the last element in a list with another list

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)

#----------------------------------------------------------------------------------------
#Extend a list without append

x = [10, 20, 30]
y = [40, 50, 60]
x[:0] =y
print(x)




	


