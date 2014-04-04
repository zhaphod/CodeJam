import os
import sys


fn = sys.argv[1]

#print (fn)

fd = open(fn, 'r')

lines = fd.readlines()

fd.close()

#print ("number of cases = " + lines[0])

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


code = {'y' : 'a', 'e' : 'o', 'q' : 'z', 'j' : 'u', 'p' : 'r', 
        'm' : 'l', 's' : 'n', 'l' : 'g', 'i' : 'd', 'c' : 'e', 
		'k' : 'i', 'd' : 's', 'x' : 'm', 'v' : 'p', 'n' : 'b',
		'r' : 't', 'a' : 'y', 'b' : 'h', 'f' : 'c', 'g' : 'v',
		'h' : 'x', 'o' : 'k', 't' : 'w', 'u' : 'j', 'w' : 'f',
		'z' : 'q', ' ' : ' '}



for i in range(1, len(lines)):
	output = "Case #" + str(i) + ": "
	chars = list(lines[i])
	for j in range(0, len(chars)):
		char = chars[j]
		if char in code.keys():
			chars[j] = code[char]
	print (output + "".join(chars).rstrip('\n'))


for let in alph:
	if let not in code.values():
		#print ("letter missing = " + let)
		pass
	
print  (code)