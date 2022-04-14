#!/usr/bin/python
import sys

#1. open textfile
textfile=open('textfile.txt','r')

dic={}

#2. read file line-by-line
lines=textfile.readlines()

for i in range (len(lines)) :
	#3. split only word
	
	#word=lines[i].split(".,!@#$%^&*/n ")
	word=lines[i].split()
	for x in word:
		x.lower()
		dic[x]=dic.get(x,0)+1
		#dicSorted=sorted(dic.dicsorted())
		#if x in dic:
			#dic[x]+=1
		#else:
			#dic[x]=1
#dicSorted=sorted(dic.items(), key=lambda y: y[1], reverse=True)

dicSorted = sorted(dic.items(), 
                              reverse=True, 
                              key=lambda item: item[1])


for key, value in dicSorted :
    print(key, value)

#for i,j in dicSorted.items():
	#print('{:10} {:>6}'.format(i,j))
	#print(i,j)
#print(dicSorted)	

#for key, value in dicSorted.items():
	#print(key, value)
