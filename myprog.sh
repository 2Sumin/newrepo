#!/bin/bash

#1. create temp dir
mkdir -p temp
echo "...create temp directory..."

#2. copy num1,num2,cal.sh
cp -p num1.txt temp/num1.txt
cp -p num2.txt temp/num2.txt
cp -p cal.sh temp/cal.sh
echo "...copy files to temp directory..."

#3. select menu
PS3='select menu : '
select val in "add" "sub" "div" "mul" 
do

	#4. set parameter
	if [ "$val" == "add" ]; then
		val1=1
	fi
	if [ "$val" == "sub" ]; then
		val1=2
	fi
	if [ "$val" == "div" ]; then
		val1=3
	fi
	if [ "$val" == "mul" ]; then
		val1=4
	fi
	echo "...$val selected..."
	echo "...run calculater..."

	#5. run cal.sh
	./cal.sh $val1
	break
done






