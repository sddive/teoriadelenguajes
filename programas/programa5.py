# -*- coding: utf-8 -*-
import re
import sys
from programa4 import programa4

def programa5(texto): 
	listaResultado = []
	match = re.search(r'(?<=var)[^\)]*?(?=begin)',texto,flags=re.DOTALL|re.I)
	if match is not None:
		variables = re.findall(r'\w+\s*?(?=,|:)',match.group(),flags=re.DOTALL)
		for va in variables:
			cant = len(re.findall('(?<!\w)' +va.strip()+ '(?!\w)',texto,flags=re.DOTALL))
			tupla = (re.sub(r'\'|\"','',va.strip()),cant-1)
			listaResultado.append(tupla)
	return listaResultado

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    lista = programa5(programa4(datos))
    f = open(archivo_salida, 'w')
    salida = ''
    for tupla in lista:
	    salida = salida +'('+ tupla[0] +','+ str(tupla[1]) + ')' + '\n'
    f.write(salida)
    f.close()
