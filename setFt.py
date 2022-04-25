#!/usr/bin/python
import sys

#1. input integer list
listA=input()
listB=input()

#2. convert list into set
setA=map(int,listA.split())
setB=map(int,listB.split())
setA=set(setA)
setB=set(setB)

#3. set union, intersection
setUnion=setA.union(setB)
setIntersection=setA.intersection(setB)

if __name__=='__main__':
	print(setUnion)
	print(setIntersection)
