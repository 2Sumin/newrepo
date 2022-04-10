#!/usr/bin/python
import sys

if __name__=="__main__":

#1. open textfile
	text=open("textfile.txt","r")

#dictionary
	dic={}

	while True:
	#2. read file line-by-line
		line=text.readline()
		if not line:
			break
	
	#3. split only word
		word=line.split(" ")

		for x in word:
			x.lower()
			#dic[x]=dic.get(x,0)+1
			if x in dic:
				dic[x]+=1
			else:
				dic[x]=1
#dicSorted=sorted(dic.items(), key=lambda y: y[1], reverse=True)

	for i,j in dic.items():
		print("%s %d"%(i,j))
	
