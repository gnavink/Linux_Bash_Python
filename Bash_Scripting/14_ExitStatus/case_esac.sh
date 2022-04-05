#!/bin/bash
#
#This script outputs the number of files in a directory
#Usage: ./4_case yes

VAR=$1
RESULT=0
echo parsing the argument
echo "" 

case $VAR in

    yes)
        echo command is valid
        RESULT=1
    ;;
    no | nee)
        echo invalid command
    ;;

    *)
    echo Enter yes or no
    ;;

esac


exit 0

