#! /bin/bash 

# Describe commands: Demonstrate the different kinds of commands

count_unique_users () {
	who | awk '{ print $1 }' | sort -u | wc -l
}

for i in cd read pwd \
         test printf \
         count_unique_users \
	 ls who sort 
	  
do
	type $i		# built-in command describing other commands
done
