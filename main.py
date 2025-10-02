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
players = [("Sally", 95), ("Toby", 88), ("Sandeep", 10), ("Zainab", 5)]


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
print(f"Average: {None}") 