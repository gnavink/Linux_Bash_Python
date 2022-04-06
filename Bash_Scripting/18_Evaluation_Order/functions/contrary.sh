#! /bin/bash

today=$(date '+%A')
if [ "$today" == Monday ]
then
	# feeling contrary
	echo () {
		printf "I don't wanna say '%s'!\n" "$*"
		return 1
	}
fi

echo Hello world
