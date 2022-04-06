#! /bin/bash

if grep azureuser /etc/passwd > /dev/null || grep navin /etc/passwd > /dev/null
then
	echo user azureuser or navin exists
fi

