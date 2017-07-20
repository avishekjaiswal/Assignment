email = raw_input("email address? ")
print ("The company's name is: {} ".format(email.partition('@')[-1].rpartition('.')[0]))
 