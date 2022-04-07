#! /bin/bash

printf 'Simple output - note the \\n at the end is a newline\n'
read junk

printf 'You cannot use \\c in format strings\n'
read junk

printf 'You can use \\c in argument strings: %b - rest ignored\n' 'testing\c'
read junk

printf 'Enter your name: '
read name
echo "Nice to meet you, $name."

printf '\n'
