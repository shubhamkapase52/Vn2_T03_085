text = 'bat ball'

# replace b with c
replaced_text = text.replace('b', 'c')
print(replaced_text)

#if else
# if text != replaced_text:
#     print("replaced")
# else:
#     print("not replace")

#by using for loop
for x in replaced_text:
    if x=='c':
     print(x)
#by using function:

def replace():
    text = 'bat ball'
    replaced_text = text.replace('b', 'c')
    return (replaced_text)
    
print(replace())



    
