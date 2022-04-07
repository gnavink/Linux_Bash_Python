#! /bin/bash 

# Demonstrate accessing arguments with $1 ... $9, $@, $*, "$@" and "$*"

printf 'Number of arguments is: %d\n\n' $#

printf 'First argument is: %s\n\n' "$1"

echo '$*: All arguments are: ' $*
./args-01-show-count.sh $*
echo

echo '$@: All arguments are: ' $@
./args-01-show-count.sh $@
echo

echo '"$*": All arguments are: ' "$*"
./args-01-show-count.sh "$*"
echo

echo '"$@": All arguments are: ' "$@"
./args-01-show-count.sh "$@"
