a=int(input("enter the first number"))
b=int(input("enter the second number"))
 
def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y
a,b=swap(a,b)
print("a= {0} and b ={1}".format(a,b))

