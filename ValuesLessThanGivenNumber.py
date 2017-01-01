a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#Code to print list that has values less than 5
new_list = []

for a in a_list:
	if (a<5):
		new_list.append(a)
		
print new_list

#Code to print list that has values less than the given number
num = int(raw_input("Enter a number: "))

new_list2=[]

for a in a_list:
	if (a<num):
		new_list2.append(a)
		
print new_list2
