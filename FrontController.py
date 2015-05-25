# -*- coding: utf-8 -*-
import os
import sys
import BaseHTTPServer

NOMBRE_SERVIDOR = 'localhost'
PUERTO = 8000

comandos = ['iniciar', 'parar', 'ayuda']

if len(sys.argv) > 1:
	print "Tienes argumentos"
else:
	print "no hay argumentos"