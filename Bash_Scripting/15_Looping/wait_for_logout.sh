#! /bin/sh

# wait_for_logout --- wait for a user to logout

user=$1

while true
do
	if who | grep "$user" > /dev/null
	then
		sleep 5
		continue
	else
		break
	fi
done

echo "$user is now logged out!"
exit 0
