
def prisoners_dilemma():
    # Get choices from the players
    player_a = input("Player A, enter your choice (cooperate/defect): ").strip().lower()
    player_b = input("Player B, enter your choice (cooperate/defect): ").strip().lower()

    # Determine the outcomes
    if player_a == "cooperate" and player_b == "cooperate":
        outcome = (-1, -1)
    elif player_a == "cooperate" and player_b == "defect":
        outcome = (-3, 0)
    elif player_a == "defect" and player_b == "cooperate":
        outcome = (0, -3)
    elif player_a == "defect" and player_b == "defect":
        outcome = (-2, -2)
    else:
        print("Invalid input. Choices must be 'cooperate' or 'defect'.")
        return
    
    # Display the result
    print(f"\nResults:")
    print(f"  Player A chose: {player_a}")
    print(f"  Player B chose: {player_b}")
    print(f"  Payoff: Player A: {outcome[0]} points, Player B: {outcome[1]} points")
    
# Run the game
prisoners_dilemma()
