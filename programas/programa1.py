import re
import sys
import os
import glob

if __name__ == '__main__':

	fname = sys.argv[1]
	sys.stdout = open(sys.argv[2], 'w')

	pattern = re.compile(r'\(\*.*?\*\)|\{.*?\}|\/\/.*$|\b(if) *(.*?) +then|\b(while) *(.*?) +do|\b(for) *(.*?) +do', re.DOTALL)

	matches = pattern.findall(open(fname,'r').read())
	currentMatch = ''
	ifMatchs = [match for match in matches if match[0] == 'if']
	if(len(ifMatchs) > 0):
		print('if:')
		for match in ifMatchs:
			print(match[1])

	forMatchs = [match for match in matches if match[4] == 'for']
	if(len(forMatchs) > 0):
		print('for:')
		for match in forMatchs:
			print(match[5])		

	whileMatchs = [match for match in matches if match[2] == 'while']
	if(len(whileMatchs) > 0):
		print('while:')
		for match in whileMatchs:
			print(match[3])
	

