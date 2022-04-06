#! /bin/bash

# Snippet of code that might be used in a .profile to
# choose a terminal type. (Welcome back to the 1990s!)

PS3='terminal? '
select term in gl35a t2000 s531 vt99
do
	echo "REPLY was >$REPLY<"	# debugging

	if [ -n "$term" ]
	then
		TERM=$term
		echo TERM is $TERM
		export TERM
		break
	else
		echo 'invalid.'
	fi
done
