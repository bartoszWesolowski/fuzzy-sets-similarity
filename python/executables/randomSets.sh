#!/bin/sh

a=0

while [ $a -lt 70 ]
do
   echo $a
   python gerateFuzzySet.py -file randomSets.txt --appendToFile -n 100
   a=`expr $a + 1`
done
