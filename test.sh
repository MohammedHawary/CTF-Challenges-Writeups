#!/bin/bash


list=("item1" "item2" "item3")
# echo "${list[2]}"
echo "${#list[@]}"
list+=("asdfdfs")
echo "${#list[@]}"

x=10
echo $x
x=`expr $x + 1`
echo $x
