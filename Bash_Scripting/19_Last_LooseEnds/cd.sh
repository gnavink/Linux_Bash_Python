# cd --- change directory and set prompt

cd () {
	command cd "$@"
	_x=$(pwd)
	PS1="${_x##*/}\$ "
}
