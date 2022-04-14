#!/usr/bin/python
import sys
import re

#1. open textfile
filename=sys.argv[1]
textfile=open(filename,'r')

dic={}

#2. read file 
lines=textfile.readlines()

for i in range (len(lines)) :
	#3. split only word
	word=lines[i].split()
	for j in range (len(word)):
		re.sub('[^A-Za-z0-9]+', '', word[j])
	
	for x in word:
		x.lower()
		dic[x]=dic.get(x,0)+1
		#another method to insert in dic	
		#if x in dic:
			#dic[x]+=1
		#else:
			#dic[x]=1

#4. Sort dictionary in descending order
dicSorted = sorted(dic.items(), reverse=True,key=lambda item: item[1])

#5. print Sorted dictionary
cnt=0
final_num=int(sys.argv[2])
for key, value in dicSorted :
	if cnt == final_num:
		break
	cnt+=1	
	print('{:10} {:>6}'.format(key,value))


