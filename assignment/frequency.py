str = raw_input("\nEnter the string: ")
str = list(str)
str2 = list(set(str))
print("\nfrequencies: ")
for i in range(len(str2)):
	print("{},{}".format(str2[i],str.count(str2[i])))