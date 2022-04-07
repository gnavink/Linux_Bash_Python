#! /bin/bash 

# Process arguments using a while loop

echo Processing $# arguments

count=1
while [ $# -gt 0 ]
do
	# In a real script, do something with "$1"
	printf "\tArgument %d: '%s'\n" "$count" "$1"

	let "count = count + 1"

	shift
done
