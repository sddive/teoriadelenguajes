import re
import sys

fname = sys.argv[1]
sys.stdout = open(sys.argv[2], 'w')

pattern = re.compile(r'^\s*(.*):=.*',re.M)

matches = pattern.findall(open(fname,'r').read())

#print(matches)
for match in matches:
	print(match)
	
	
