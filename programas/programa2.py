import re
import sys
	
fname = sys.argv[1]
sys.stdout = open(sys.argv[2], 'w')

pattern = re.compile(r'\(\*.*?\*\)|\{.*?\}|\/\/.*$|\b(if) *.*?\bthen|\b(while) *.*?\bdo|\b(for) +.*? +do|\b(repeat)\b.*\buntil',re.DOTALL)
matches = pattern.findall(open(fname,'r').read())
print('if '+ str(len([match for match in matches if match[0] == 'if'])))
print('for '+ str(len([match for match in matches if match[2] == 'for'])))
print('while '+ str(len([match for match in matches if match[1] == 'while'])))
print('repeat '+ str(len([match for match in matches if match[3] == 'repeat'])))
	
	
	