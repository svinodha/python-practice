#Code for String Reverse
str = raw_input("Enter a string: ")

string_len = len(str)

str_range = range(0, string_len)

new_str = ""

#print string_len
#print str_range

for i in str_range:
	new_str+=str[string_len-1-i]
print new_str

#Code to check Palindrome
if str.lower()==new_str.lower():
	print "%s is a Palindrome" %str
else:
	print "%s is not a Palindrome" %str
