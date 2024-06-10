#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input file> <output file>"
  exit 1
fi

if [ ! -e "$1" ]; then
  echo "Error: '$1' not found."
  exit 1
fi

full_path=$1
file_name="${full_path##*/}"
python main.py $file_name output_left.pdf left
python main.py $file_name output_right.pdf right
python merge.py output_left.pdf output_right.pdf $2