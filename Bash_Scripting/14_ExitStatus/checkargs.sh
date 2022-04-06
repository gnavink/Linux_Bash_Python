#!/bin/bash

if [ "$#" -ne 2 ]
then
    echo Usage:./checkargs -f /some/file 2>&1
    exit 1
fi

exit 0

