#Code to make even number list. http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
a_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_list=[]

for a in a_list:
	if (a%2) == 0:
		even_list.append(a)
print even_list
