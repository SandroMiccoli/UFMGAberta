#!/usr/bin/python
# -*- coding: latin-1 -*-

import csv
import json

f = open( '../csv/relacaoCursoGrandeArea.csv', 'r' )

reader = csv.DictReader( f, fieldnames = ( "CURSO","UNIDADE","AREA", "GRANDE AREA", "APELIDO" ) )
out = json.dumps( [ row for row in reader ] )
output = json.loads(out)

cursos = []

for i in output:
	j = {}
	#print i
	j['curso'] = str(i['CURSO'])
	j['unidade'] = str(i['UNIDADE'])
	j['area'] = str(i['AREA']).encode('latin-1')
	j['grandearea'] = str(i['GRANDE AREA']).encode('latin-1')
	j['apelido'] = str(i['APELIDO']).encode('latin-1')
	
	cursos.append(j)

print cursos
