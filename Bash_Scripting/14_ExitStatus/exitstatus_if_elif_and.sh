#! /bin/bash

if test -f /etc/passwd && grep azureuser /etc/passwd > /dev/null
then
	echo password file exists as does user azureuser
elif test -f /etc/group && grep azureuser /etc/group > /dev/null 
then 
	echo group file exists as does user azureuser
else
	echo no passwd or group file exists also no user or group azureuser exists
fi

