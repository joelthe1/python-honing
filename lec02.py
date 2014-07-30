value = int(raw_input("Enter number for checking: "))
if value < 0 :
	print "Please enter only positive numbers"
elif (value % 2) == 0:
	print "The number is even."
else : print "The number is odd"