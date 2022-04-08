#phrase = "it marks the spot"
phrase = "X marks the spot"
for character in phrase:
    if character == "X":
        break
else:
    print("There was no 'X' in the phrase")
