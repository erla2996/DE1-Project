#!/bin/bash

# Script that splits the contents of an input file into

input_file="input_1.txt" # Change this to the input file name
output_file_base="input/input_part_"

n=0
lines_per_file=100
max_files=100

outfiles=()
for((i=0; i < max_files; i++)); do
   outfiles+=("$output_file_base$i.txt")
done

exec 5< $input_file

i=0
while read line <&5; do
   echo "$line">>${outfiles[$i]}
   i=$(($i+1))
   if (($i == 100)); then
      i=0
   fi
done

exec 5<&- # Close file handle 5
