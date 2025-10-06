def input_players_and_score(players):
    
    while True:
    
        player_name = input("Please input player name (Or \"done\"): ")

    # account for capitalization with .lower()
        if player_name.lower() == "done":
            print("Ending program. Displaying results.")
            break
    
        if player_name == "":
            print("You did not enter a name please try again.")
            continue
    
    # use .isnumeric() to see if user put a number
        player_score = input(f"Please input a score for {player_name}: ")
        if not player_score.isnumeric():
            print("Invalid score. Skipping this entry.")
            continue
        else:
        # convert player score to int afterwards so no errors since i checked if its numeric
            player_score = int(player_score)

    # creating a tuple so i can add it to original list using .append
        name_and_score = (player_name, player_score)
        players.append(name_and_score)
    