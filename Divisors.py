#Code to find the divisors of a given number. For ex, 13 is a divisor of 26 because 26 / 13 has no remainder 
number = int(raw_input("Enter a number: "))

number_range = range (1, number+1)
new_list = []

for i in number_range :
	if (number % i) == 0:
		new_list.append(i)
print "The divisors of %d are %s" %(number, new_list)
