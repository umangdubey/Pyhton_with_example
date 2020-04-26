from functools import reduce

num = [2,4,6,5,8,7,9,3,1]

even=list(filter(lambda n:n%2==0,num))    #filter use to filter the or say seprating the data

print("even",even)

odd=list(filter(lambda b:b%2!=0,num))

print("odd",odd)


doubles = list(map(lambda n:n+2,even))   #map perform operation on the data

print("doubles with +2",doubles)


sums= reduce(lambda a,b:a+b,doubles)   #reduce reduce the data to particular set

print(sums)
