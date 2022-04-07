#! /bin/bash -

Mail () {		# For demonstration purposes only
	echo Mail "$@"  
	cat
	echo
	echo ======================
	echo
}

IFS=:
while read name amount email
do
	Mail -s 'Late payment due' "$email" <<- EOF
		Dear $name,

		As of $(date '+%B %-d, %Y'), you still owe us Rs.$amount.
		Please send payment immediately.

		Sincerely,

		Mannar & Co & Sons, Inc.
	EOF

done < payments-due.txt
