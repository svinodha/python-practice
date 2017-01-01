#Code to check whether the number is Odd or Even
number1 = int(raw_input("Enter a number: "))

if (number1 % 2) == 0:
	print "%d is a even number" %number1
else:
	print "%d is an odd number" %number1

#Code to check if the number is multiple of 4
number2 = int(raw_input("Enter another number: "))
if (number2 % 4) == 0:
	print "%d is a multiple of 4" %number2
else:
	print "%d is not a multiple of 4" %number2
	
#Code to check if a number divides evenly into another number
num = int(raw_input("Enter a number: "))
check = int(raw_input("Enter another number: "))

if (check % num) == 0:
	print "%d divides evenly into %d" %(check, num)
else:
	print "%d does not divide evenly into %d" %(check, num)
