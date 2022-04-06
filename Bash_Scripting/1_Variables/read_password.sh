printf "Enter new password: "  #Prompt for input
stty -echo
read pass < /dev/tty          #Read password
printf	 "\n"
printf "Enter again: "        #Prompt again
read pass2 < /dev/tty         #Read again for verification
stty echo                     # Don't forget to turn echoing back on








