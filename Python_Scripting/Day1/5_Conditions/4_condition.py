sport = input("Enter a sport: ")

p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))

sport = sport.lower()
if p1_score == p2_score:
    print("The game is a draw.")
elif (sport == "basketball") or (sport == "golf"):
    p1_wins_bball = (sport == "basketball") and (p1_score > p2_score)
    p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
    p1_wins = p1_wins_bball or p1_wins_golf
    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")
