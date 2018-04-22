import re
import sys
from programa4 import programa4

archivo_entrada = sys.argv[1]
f = open(archivo_entrada, 'r')
datos = f.read()
sys.stdout = open(sys.argv[2], 'w')

pattern = re.compile(r'^\s*(.*):=.*',re.M)
fname = programa4(datos)

matches = pattern.findall(fname)

#print(matches)
for match in matches:
	print(match)
	
	
