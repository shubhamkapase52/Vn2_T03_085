#nth index character from string
# a=input("enter the string")
# b=a[-2:-1]
# print(b)


#if else method
# if len(a)>1:
#     print("length is greater then 1")
# else:
#     print("not")

#by using function
# def index(a):
    
#     return a[-1:]
# a=input("enter the string")
# print(index(a))

#by using class
class nth():
    def __init__(self):
        self.name=input("enter the name")
    def index(self):
        self.a=input("enter the string")
        self.b=self.a[-1:]
        print(self.b)

k=nth()
k.index()



