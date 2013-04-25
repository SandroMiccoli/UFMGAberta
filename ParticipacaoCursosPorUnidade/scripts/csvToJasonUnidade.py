#!/usr/bin/python
# -*- coding: latin-1 -*-

import csv
import json

f = open( 'porUnidade.csv', 'r' )

reader = csv.DictReader( f, fieldnames = ( "CURSO","FACE","DIREITO","ECI","FAFICH","LETRAS","FAE","BELAS ARTES","MUSICA","IGC","ARQUITETURA","ICEX","ENGENHARIA","FARMACIA","VETERINARIA","EEFFTO","ENFERMAGEM","MEDICINA","ODONTOLOGIA","ICB","ICA","REUNI" ) )
out = json.dumps( [ row for row in reader ] )
output = json.loads(out)

cursos = []

for i in output:
	j = {}
	#print i
	j['name'] = str(i['CURSO'])
	del i['CURSO']
	#print i
	
	childs = []
	for key in i.keys():
		size = "%.4f" % float(str(i[key]).replace(',','.'))
		size = int(float(size)*1000)
		children = {}
		children['name']=key.encode('utf-8')
		children['size']=size
		if (size>10):
			childs.append(children)
		#print childs
		
	#children['name'] = i[
	j['children'] = childs
	cursos.append(j)

print cursos