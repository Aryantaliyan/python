list1=[1,2,3,4,5]
list2=[2,5,6,"aryan",True]

print(type(list1))

print(list1[2])

list3=list1+list2

print(list3)

print(list3[-2])

for i in list1:
    print(f")-({i})-(",end="")
print()

if "aryan" in list2:
    print("Yes")
else:
    print("No") 

print(list3[4:-2]) #slicing

print(list3[4:-2:2]) #jump indexing

print()


######################list methods######################

#list.append
#list.sort
#list.reverse
#list.index
#list.count
#list.copy
#list.insert
#list.extend





l=[5,7,3,5,7]
print(l)
l.append(7)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(5))
print(l.count(5))
print(l.count(5))
m=l.copy()
m[0]=0
print(l)
l.insert(1,899)
print(l)
n=[55,77,88]
l.extend(n)
print(l)