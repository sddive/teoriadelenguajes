# -*- coding: utf-8 -*-
import re
import sys

def programa4(texto):
	salida = ""
	sinCom = re.sub(r'\{.*?}|\(\*.*?\*\)|\/\/[^\n]*','',texto,flags=re.DOTALL)
	return sinCom            

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa4(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
