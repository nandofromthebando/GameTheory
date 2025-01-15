import Players_To_Test  # Ensure only one import.

def prisoners_dilemma(player_a, player_b):
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
        return None  # Return None explicitly in case of invalid input.
    
    return outcome[0], outcome[1]
    
# Run the game
print("Prisoner's Dilemma Simulation: Sample size of 40 rounds per scenario")
print("Player 1 (Random Choice) is compared against all strategies of Player 2.")

# List of strategies
strategies = [
    ("Always Cooperate", lambda choice: Players_To_Test.cooperate()),
    ("Always Defect", lambda choice: Players_To_Test.defect()),
    ("Opposites", Players_To_Test.opposites),  # Requires Player 1's choice.
    ("Mirrored", Players_To_Test.mirror),     # Requires Player 1's choice.
    ("Cooperate First Half (Then Random)", lambda i: Players_To_Test.cooperate() if i <= 19 else Players_To_Test.rand_option()),
    ("Cooperate First Half (Then Defect)", lambda i: Players_To_Test.cooperate() if i <= 19 else Players_To_Test.defect()),
    ("Defect First Half (Then Cooperate)", lambda i: Players_To_Test.defect() if i <= 19 else Players_To_Test.cooperate()),
    ("Random Choice", lambda choice: Players_To_Test.rand_option()),
]

# Simulate all scenarios
for name, strategy in strategies:
    score1, score2 = 0, 0
    for i in range(40):
        player1_choice = Players_To_Test.rand_option()  # Generate Player 1's choice.
        
        if callable(strategy) and name in ["Opposites", "Mirrored"]:
            # Pass Player 1's choice to strategies that depend on it.
            choice2 = strategy(player1_choice)
        elif callable(strategy):
            # Pass the index for time-dependent strategies.
            choice2 = strategy(i) if name in ["Cooperate First Half (Then Random)", "Cooperate First Half (Then Defect)", "Defect First Half (Then Cooperate)"] else strategy(None)
        else:
            choice2 = strategy  # For fixed strategies like always cooperate/defect.

        outcome = prisoners_dilemma(player1_choice, choice2)
        if outcome is not None:  # Ensure valid outcomes before updating scores.
            outcome1, outcome2 = outcome
            score1 += outcome1
            score2 += outcome2
    print(f'Random Choice: {score1} {name}: {score2}')
