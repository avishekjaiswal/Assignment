str = raw_input("Enter the string ")
list = str.split(" ")
list = [x for x in list if x.isdigit()]
print list
