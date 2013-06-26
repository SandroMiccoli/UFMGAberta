#!/usr/bin/python
# -*- coding: latin-1 -*-

import csv
import json

f = open( '../csv/alunos.csv', 'r' )
reader = csv.DictReader( f, fieldnames = ( "curso","ID_ALUNO","ADMISSAO","2008/1","2008/2","2009/1","2009/2","2010/1","2010/2","2011/1","2011/2","2012/1","2012/2" ) )
out = json.dumps( [ row for row in reader ] )
print out
