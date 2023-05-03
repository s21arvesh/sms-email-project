from array import *

list1=[1,2,3,635,12,546,0]

print(sorted(list1))
list1.sort(reverse=True)
print(list1.count(2))

dict={'neymar':'brasil','messi':'argentina','ronaldo':'portugal'}
print(dict)

print(dict.items())

set1 = {1,2,3,5,4,4,4,}
set2 = {5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

# OPERATIONS IN SETS - union() , intersection() , difference() , symmertric_difference()

arr = array('i',[]) #creating an empty array
n = int(input("ENTER THE RANGE OF ARRAY"))

for i in range(n):

    x = (int(input("ENTER THE NEXT VALUE")))
    arr.append(x)

print(arr)
