#! /bin/bash -

type cd
echo defining cd function

function cd () {
	command cd "$@"
	printf "Moved to %s\n" $(pwd)
}

type cd

cd /usr/local/bin

