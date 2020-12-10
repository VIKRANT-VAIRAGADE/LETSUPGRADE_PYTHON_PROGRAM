lst1 = [1,2,3,4,5,6,7,8]
lst2 = ["v","i",'k','r','a','n','t']
lst3=["vikrant",1998]

print(len(lst1))  # length
print(type(lst3))  # type
print(lst2[1:4])
lst3[1] = 2000 # change the item
print(lst3)
lst3.insert(1,'vairagade') # adding new item at particular position
print(lst3)
lst2.append("orange") # adding new item at end
print(lst2)
lst1.extend(lst2)  # to adding item from lst2 in lst1
print(lst1)
newlst = lst3 + lst2 #adding lists
print(newlst)
newlst2 =lst1*2
print(newlst2)
lst1.remove(1)
print(lst1)
lst2.sort()
print(lst2)
lst2.remove('orange')
print(lst2)