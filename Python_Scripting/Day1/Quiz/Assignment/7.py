#Run in an infinite loop until the user types "q" or "Q"
while True:
    user_input = input('Type "q" or "Q" to quit: ')
    if user_input.upper() == "Q":
        break
