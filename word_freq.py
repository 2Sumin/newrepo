#!/usr/bin/python
import sys

#1. open textfile
textfile=open('textfile.txt','r')

#dictionary
dic={}

while True:
	#2. read file line-by-line
	line=textfile.readline()
	if not line:
		break
	#3. split only word
	word=line.split('.,!@#$%^&*/')


