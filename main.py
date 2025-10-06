from score_stats import calculate_avg_score
from output import output_player_summary
from input import input_players_and_score
from output import get_highest_score
from output import get_lowest_score

# store players as a list of tuples
players = []
input_players_and_score(players)

# players = [("Sally", 95), ("Toby", 90), ("Sandeep", 10), ("Zainab", 5)]

highest_player = ()
lowest_player = ()

# setup variables to store summary values
num_players = len(players)
highest_score_player = get_highest_score(players, highest_player)
lowest_score_player = get_lowest_score(players, lowest_player)
average_score = calculate_avg_score(players)

# Output player summary
output_player_summary(num_players, highest_score_player, lowest_score_player, average_score)
