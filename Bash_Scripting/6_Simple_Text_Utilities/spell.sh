#! /bin/sh

sort -u /usr/share/dict/words > list.words

cat "$@" |
	tr '[:space:][:punct:]' '\n' | \
		tr '[:upper:]' '[:lower:]' |  \
			sort -u | \
				comm -23 - list.words
