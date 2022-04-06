#! /bin/bash

trap 'rm -f $tmpfile' EXIT

tmpfile=$(mktemp -p /tmp myprog.XXXXXXXXXXXX) || exit 1

echo this is some data > $tmpfile

# Show contents. In a real script, do some real work.
ls -l $tmpfile
echo
cat $tmpfile

# Script exits here. Trap on EXIT cleans up.
