#!/bin/bash

function1() {
   echo 'Argument 1 is:' "$1"
   echo 'Num Args is:' $#
   echo 'Args are: ' ""$@
}


function1 Navin Kumar 45


