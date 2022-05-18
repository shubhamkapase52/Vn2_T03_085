# str="the world is beautiful"
# b=str.swapcase()
# print(b)

#by using if else
# if 'A' in b:
#     print("swapping is done")
# else:
#     print("not swapping")

def swap(string):
      return string[-1:] + string[1:-1] + string[:1]
 
# take string from user
str1 = input("Please Enter String : ")
 
print (swap(str1))
