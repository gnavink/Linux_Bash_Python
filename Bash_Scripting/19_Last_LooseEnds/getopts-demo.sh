#! /bin/bash

# set flag vars to empty
file=   verbose=   quiet=   long=

while getopts f:vql opt
do
    case $opt in            # Check option letter
    f)     file=$OPTARG
           ;;
    v)     verbose=true
           quiet=
           ;;
    q)     quiet=true
           verbose=
           ;;
    l)     long=true
           ;;
    esac
done

shift $((OPTIND - 1))       # Remove options, leave arguments

echo "file=$file   verbose=$verbose   quiet=$quiet   long=$long"

echo Remaining arguments: "$@"
