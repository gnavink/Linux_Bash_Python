#! /bin/bash

a=something
if [ -z "$a" ]
then
	echo a is empty
else
	echo a is $a
fi

