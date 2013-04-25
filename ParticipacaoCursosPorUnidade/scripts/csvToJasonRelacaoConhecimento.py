#!/usr/bin/python
# -*- coding: latin-1 -*-

import csv
import json

f = open( 'relacaoCursoUnidadeAreaConhecimento.csv', 'r' )

reader = csv.DictReader( f, fieldnames = ( "CURSO","UNIDADE","AREA" ) )
out = json.dumps( [ row for row in reader ] )
output = json.loads(out)

cursos = []

for i in output:
	j = {}
	#print i
	j['curso'] = str(i['CURSO'])
	j['unidade'] = str(i['UNIDADE'])
	j['area'] = str(i['AREA']).encode('latin-1')
	
	cursos.append(j)

print cursos
