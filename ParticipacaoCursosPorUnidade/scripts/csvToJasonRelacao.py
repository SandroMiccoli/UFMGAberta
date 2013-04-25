#!/usr/bin/python
# -*- coding: latin-1 -*-

import csv
import json

f = open( 'relacaoCursoUnidade.csv', 'r' )

reader = csv.DictReader( f, fieldnames = ( "CURSO","UNIDADE" ) )
out = json.dumps( [ row for row in reader ] )
output = json.loads(out)

cursos = []

for i in output:
	j = {}
	#print i
	j['curso'] = str(i['CURSO'])
	j['unidade'] = str(i['UNIDADE'])
	
	cursos.append(j)

print cursos
