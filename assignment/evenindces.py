from __future__ import print_function
str = raw_input("\nEnter the string ")
str = list(str)
for i in range(len(str)):
	if(i%2 == 0):
		print (str[i], end = '')
print("")