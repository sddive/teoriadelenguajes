# -*- coding: utf-8 -*-
import re
import sys

def programa4(texto):
	salida = ""
	sinCom1 = re.sub(r'\{.*?}|\(\*.*?\*\)','',texto,flags=re.DOTALL)
	sinCom2 = re.sub(r'\/\/.*','',sinCom1)
	return sinCom2            

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
