#! /bin/sh

# wait_for_user --- wait for a user to login

user=$1

until who | grep "$user" > /dev/null
do
	sleep 5
done

echo "$user is now logged on!"
exit 0
