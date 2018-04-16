#!/bin/sh
cat p4file | while read LINE
do
echo $LINE
p4c-bmv2 $LINE --json ${LINE}.json --p4-v1.1
done
