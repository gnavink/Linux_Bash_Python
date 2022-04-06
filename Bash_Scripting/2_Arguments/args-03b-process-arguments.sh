#! /bin/bash 

# Process arguments using a while loop

echo Processing $# arguments

count=1
# default is for i in "$@"
for i	

do
	# In a real script, do something with "$i"
	printf "\tArgument %d: '%s'\n" "$count" "$i"

	let "count = count + 1"
done

printf "$0\n"
