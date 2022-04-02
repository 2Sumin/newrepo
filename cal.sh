#!/bin/bash

#1. read num1.txt, num2.txt

declare -a arr
while read line; do
	num1=$line
done < num1.txt

while read line; do
	num2=$line
done<num2.txt

#2. operation_1)no parameter
if [[ -z "$1" ]]; then
	echo "...none operator parameter..."

	PS3="select menu : "	
	select val in "add" "sub" "div" "mul"
	do
		break
	done

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
val2=$val1

#2. operation_2)parameter
else
	val2=$1
	if [ "$1" = "1" ]; then
		val=add
	fi
	if [ "$1" = "2" ]; then
		val=sub
	fi
	if [ "$1" = "3" ]; then
		val=div
	fi
	if [ "$1" = "4" ]; then
		val=mul
	fi

fi

#3. print result
if [ "$val2" = "1" ]; then
	result=$(($num1 + $num2))

fi
if [ "$val2" = "2" ]; then
	result=$(($num1 - $num2))

fi

if [ "$val2" = "3" ]; then
	result=$(($num1 / $num2))
fi

if [ "$val2" = "4" ]; then
	result=$(($num1 * $num2))
fi

echo
echo "num1 : $num1"
echo "num2 : $num2"
echo "op : $val"
echo "result : $result"

exit 0
