	= () {				# string comparison
		case $1 in
		"$2")  return 0 ;;
		esac
		return 1
	}

pattern='ab*'
stringval='abc'
echo $pattern
echo $stringval

if =  $stringval  "$pattern"
then
	echo matches
else
	echo not matching
fi

