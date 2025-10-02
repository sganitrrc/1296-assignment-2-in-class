"""
input example:

Enter player name (or "done"): Alice
Enter score for Alice: 95
Enter player name (or "done"): Bob
Enter score for Bob: notanumber
Invalid score. Skipping this entry.
Enter player name (or "done"): Cara
Enter score for Cara: 88
Enter player name (or "done"): done
"""
# store players as a list of tuples
players = [("Sally", 95), ("Toby", 90), ("Sandeep", 10), ("Zainab", 5)]

# setup variables to store summary values
highest_score_player = (None, 0)
lowest_score_player = (None, 0)
average_score = 0


## pull the scores into a separate list
# declare a new variable to hold a list of scores
player_scores = []
score_total = 0

# iterate over the players list
# add each score to the new list
for player in players:
    player_scores.append(player[1])
    # add all the scores together
    score_total += player[1]

# print(score_total)
# print(player_scores)
# find the average
# divide by the number of scores
# set the value of average_score
average_score = score_total / len(player_scores)


"""
output example:

=== Summary ===
Players: 2
Highest: Alice — 95
Lowest:  Cara — 88
Average: 91.5
"""

# Output player summary
print("=== Summary ===")
print(f"Players: {len(players)}")
print(f"Highest: {None}") # Sally - 95
print(f"Lowest:  {None}") # Zainab - 5
print(f"Average: {average_score}") 