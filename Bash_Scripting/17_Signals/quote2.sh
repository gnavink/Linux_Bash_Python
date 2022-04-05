#! /bin/sh

x='original x'

trap 'echo x is $x' EXIT

x='new x'

sleep 2
