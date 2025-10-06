def output_player_summary(num_players, highest_score, lowest_score, average_score):
    print("=== Summary ===")
    print(f"Players: {num_players}")
    print(f"Highest: {highest_score[0]} - {highest_score[1]}")
    print(f"Lowest:  {lowest_score[0]} - {lowest_score[1]}")
    print(f"Average: {average_score}") 

def get_highest_score(players, highest_player):

    highest_player_score = 0
    
    for player in players:

        if player[1] > highest_player_score:
            highest_player_score = player[1]
            highest_player = player

    return highest_player

def get_lowest_score(players, lowest_player):

    lowest_player_score = players[0][1]
    
    for player in players:

        if player[1] < lowest_player_score:
            lowest_player_score = player[1]
            lowest_player = player

    return lowest_player
