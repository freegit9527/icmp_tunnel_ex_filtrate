#encoding=utf-8

import re 
import os 
import sys

file=sys.argv[1]
f = open(file, "r")
f1 = open('test.txt', 'w+')
pattern = re.compile(r'(?<=\$\$START\$\$).*')  
m=''
n=''
for line in f:
	searchObj = re.search( r'\$\$START\$\$', line)
	if searchObj:
		m = pattern.findall(line)
		print m[0]
		if m[0] != n:
			f1.write(str(m[0])+'\n')
			n = m[0]

os.system('base64 -d  test.txt >> result.txt')
