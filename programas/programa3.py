import re
import sys

fname = sys.argv[0]

pattern = re.compile(r'^\s*(.*):=.*',re.M)

matches = pattern.findall(open('../entradas/entrada3.txt','r').read())

#print(matches)
for match in matches:
	print(match)
	
	
