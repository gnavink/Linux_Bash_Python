#! /bin/sh

# wait_for_user --- wait for a user to login
#
# Usage: wait_for_user user sleep-time

wait_for_user () {
	if [ $# != 2 ]
	then
		echo Usage: wait_for_user user sleep-time 1>&2
		return 1
	fi

	until who | grep "$1" > /dev/null
	do
		# debugging:
		echo $1 is not logged in yet, sleeping $2 seconds

		sleep $2
	done

	# debugging:
	echo $1 is here!

	return 0
}

sleeptime=${2:-10}

# ....

wait_for_user $1 5

# ....
