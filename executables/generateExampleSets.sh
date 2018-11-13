#!/bin/sh

appendToFile=" -file example-sets.txt --appendToFile "

# random sets
python generateFuzzySet.py $appendToFile -n 100 -comment "Totally random set with 100 elements"
python generateFuzzySet.py $appendToFile -n 20  --smoothRandom -maxDiff 0.05 -comment "Smoothed random set with 20 elements"
python generateFuzzySet.py $appendToFile -n 200  --smoothRandom -maxDiff 0.05 -comment "Smoothed random set with 200 elements"

# # values smaller than 0.5
python generateFuzzySet.py $appendToFile -n 10 -max 0.5 --smoothRandom -maxDiff 0.1 -comment "Smoothed random set with 10 elements, all values smaller than 0.5"
python generateFuzzySet.py $appendToFile -n 10 -max 0.5 --smoothRandom -maxDiff 0.15 -comment "Smoothed random set with 10 elements, all values smaller than 0.5"

python generateFuzzySet.py $appendToFile -n 50 -max 0.5 --smoothRandom -maxDiff 0.05 -comment "Smoothed random set with 50 elements, all values smaller than 0.5"
python generateFuzzySet.py $appendToFile -n 50 -max 0.5 --smoothRandom -maxDiff 0.05 -comment "Smoothed random set with 50 elements, all values smaller than 0.5"

python generateFuzzySet.py $appendToFile -n 200 -max 0.5 --smoothRandom -maxDiff 0.05 -comment "Smoothed random set with 200 elements, all values smaller than 0.5"
python generateFuzzySet.py $appendToFile -n 200 -max 0.5 --smoothRandom -maxDiff 0.05 -comment "Smoothed random set with 200 elements, all values smaller than 0.5"

python generateFuzzySet.py $appendToFile -n 10 -max 0.5 --randomWithRescaled -maxDiff 0.1 -rescaleY 2.0 -comment "Smoothed random set with 10 elements, all values smaller than 0.5 and second one rescaled by 2.0"

python generateFuzzySet.py $appendToFile -n 50 -max 0.5 --randomWithRescaled -maxDiff 0.1 -rescaleY 2.0 -comment "Smoothed random set with 50 elements, all values smaller than 0.5 and second one rescaled by 2.0"

python generateFuzzySet.py $appendToFile -n 200 -max 0.5 --randomWithRescaled -maxDiff 0.1 -rescaleY 2.0 -comment "Smoothed random set with 200 elements, all values smaller than 0.5 and second one rescaled by 2.0"

python generateFuzzySet.py $appendToFile -n 20 --triangularRescaled -rescaleX 2.0 -comment "Small triangular set and it\'s and same set resized by 2 in x scale"

python generateFuzzySet.py $appendToFile -n 200 --triangularRescaled -rescaleX 2.0 -comment "Large triangular set and it\'s and same set resized by 2 in x scale"

python generateFuzzySet.py $appendToFile -n 20 --triangularRescaled -rescaleX 2.0 -comment "Large triangular set and it\'s and same set resized by 2 in x scale"

python generateFuzzySet.py $appendToFile -n 20 --triangularRescaled -rescaleY 2.0 -comment "Small triangular set and it\'s and same set resized by 2 in y scale"

python generateFuzzySet.py $appendToFile -n 200 --triangularRescaled -rescaleY 2.0 -comment "Large triangular set and it\'s and same set resized by 2 in y scale"

python generateFuzzySet.py $appendToFile -n 200 --triangularRescaled -rescaleY 2.0  -rescaleX 2.0 -comment "Large triangular set and it\'s and same set resized by 2 in y and x scale"

python generateFuzzySet.py $appendToFile -n 20 --singleton -value 0.5 -comment "Small constant set with value each value equal to 0.5"
python generateFuzzySet.py $appendToFile -n 20 --singleton -value 1.0 -comment "Small constant set with value each value equal to 1"
python generateFuzzySet.py $appendToFile -n 20 --singleton -value 0.0 -comment "Small constant set with value each value equal to 0"
