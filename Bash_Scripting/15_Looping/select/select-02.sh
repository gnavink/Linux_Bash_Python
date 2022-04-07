#! /bin/bash

# Snippet of code that might be used in a .profile to
# choose a terminal type. (Welcome back to the 1990s!)

echo 'Select your terminal type:'
PS3='terminal? '
select term in \
	'Givalt GL35a' \
	'Tsoris T-2000' \
	'Shande 531' \
	'Vey VT99'
do
	case $REPLY in
	1) TERM=gl35a ;;
	2) TERM=t2000 ;;
	3) TERM=s531 ;;
	4) TERM=vt99 ;;
	*) echo 'invalid.' ;;
	esac
	if [[ -n $term ]]; then
		echo TERM is $TERM
		export TERM
		break
	fi
done
