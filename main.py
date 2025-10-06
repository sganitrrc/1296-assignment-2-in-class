from score_stats import calculate_avg_score
from output import output_player_summary
from input import input_players_and_score
from output import get_highest_score
from output import get_lowest_score
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
#players = []
#input_players_and_score(players)
#print(players)
players = [("Sally", 95), ("Toby", 90), ("Sandeep", 10), ("Zainab", 5)]

highest_player = ()
lowest_player = ()

# setup variables to store summary values
num_players = len(players)
highest_score_player = get_highest_score(players, highest_player)
lowest_score_player = get_lowest_score(players, lowest_player)
average_score = calculate_avg_score(players)

# Output player summary
output_player_summary(num_players, highest_score_player[1], lowest_score_player[1], average_score)
# some random change