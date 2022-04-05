#! /bin/sh

# wait_for_user --- wait for a user to login

user=$1

while true
do
	if who | grep "$user" > /dev/null
	then
		break
	fi

	sleep 5
done

echo "$user is now logged on!"
exit 0
