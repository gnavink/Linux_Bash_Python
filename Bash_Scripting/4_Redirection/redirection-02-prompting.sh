#! /bin/bash 

pass=x pass2=y					#Set the values so that until loop returns false initially
until [ "$pass" = "$pass2" ]
do
	stty -echo				# Turn off echoing

	printf "Enter new password: "		# Prompt for input

	read pass < /dev/tty			# Read password

	printf "\nEnter again: "		# Prompt again

	read pass2 < /dev/tty			# Read again for verification

	stty echo				# Turn echoing back on

	echo
	if [ "$pass" = "$pass2" ]
	then
		echo Passwords match
	else
		echo Passwords do not match
	fi
done
