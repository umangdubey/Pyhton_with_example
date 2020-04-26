

def update(x):
    print(id(x))  #id of x equal to a i.e 10001

    x=5
    print(id(x))  #here id of x is different because update value storedin differnt memmor
    print("x",x)


a=10
print(id(a))  #eg id of a =10001
update(a)
print("a",a)
print(id(a))  #eg id of a =10001



#in python call by value and call by reference there is no concept of that because in python variable use of label 
