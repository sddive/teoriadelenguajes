import re
import sys



fname = sys.argv[0]

pattern = re.compile(r'\b(if) *.* +then|\b(while) *.* +do|\b(for) *.* +do|\b(repeat) *.* +until')

matches = pattern.findall(open('../entradas/entrada1.txt','r').read())

print('if '+ str(len([match for match in matches if match[0] == 'if'])))
print('for '+ str(len([match for match in matches if match[2] == 'for'])))
print('while '+ str(len([match for match in matches if match[1] == 'while'])))
print('repeat '+ str(len([match for match in matches if match[3] == 'repeat'])))
	
	
