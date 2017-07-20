list1 = [142,214,355,730,838,120,155,32]
list1 = [x for x in list1 if list1.index(x) % 2 != 0]
print("\nThe given list [12,24,35,70,88,120,155] without 0th, 2nd, 4th and 6th numbers is: ")
for i in range(len(list1)):
	print list1[i],