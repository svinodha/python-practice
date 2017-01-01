import sys
import datetime

name = raw_input("Please enter your name: ")

age = int(raw_input("Please enter your age: "))

def age_calc(age):
	if (age<100):
		remaining_years = 100-age
		current_time = datetime.datetime.now()
		current_year = int(current_time.year)
		hund_year = current_year+remaining_years
		return hund_year
		
		
hundred_year = age_calc(age)

print "%s, You will turn hundred years old in %d" %(name,hundred_year)

#Code to print the message n times
count_number = int(raw_input("How many times do you want to print the previous message?"))

initial_count = 0
while (initial_count<count_number):
	print "%s, You will turn hundred years old in %d" %(name,hundred_year)
	initial_count = initial_count+1

#Another method to print n times	
another_count = int(raw_input("Again, How many times do you want to print the previous message?"))
	
print (another_count* ("%s, You will turn hundred years old in %d\n" %(name,hundred_year)))
