#! /bin/sh

file=$1
if [ -L "$file" ]
then
	echo $file is a symbolic link
elif [ -f "$file" ]
then
	# note - not elif ; each attribute is orthogonal

	if [ -r "$file" ]
	then
		echo $file is readable
	fi
	
	if [ -w "$file" ]
	then
		echo $file is writeable
	fi

	if [ -x "$file" ]
	then
		echo $file is executable
	fi
elif [ -d "$file" ]
then
	echo $file is a directory
else
	echo $file is neither a regular file, a directory, nor a symlink
fi
