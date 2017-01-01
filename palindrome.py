#Code to check whether the given string is a Palindrome
str = raw_input("Enter a String: ")

str2=str[ : :-1]

if str.lower()==str2.lower():
	print "%s is a Palindrome" %str
else:
	print "%s is not a Palindrome" %str
