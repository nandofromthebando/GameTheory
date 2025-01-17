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
    ("Cooperate First Half (Then Mirror)", lambda i, choice: Players_To_Test.cooperate() if i <= 19 else Players_To_Test.mirror(choice)),
    ("Cooperate First Half (Then Opposites)", lambda i, choice: Players_To_Test.cooperate() if i <= 19 else Players_To_Test.opposites(choice)),
    ("Defect First Half (Then Random)", lambda i: Players_To_Test.defect() if i <= 19 else Players_To_Test.rand_option()),
    ("Defect First Half (Then Mirror)", lambda i, choice: Players_To_Test.defect() if i <= 19 else Players_To_Test.mirror(choice)),
    ("Defect First Half (Then Opposites)", lambda i, choice: Players_To_Test.defect() if i <= 19 else Players_To_Test.opposites(choice)),
    ("Opposites Every Other", lambda i, choice: Players_To_Test.opposites(choice) if i % 2 == 0 else choice),
    ("Mirror Every Other", lambda i, choice: Players_To_Test.mirror(choice) if i % 2 == 0 else choice),
    ("Opposites First Half (Then Mirror)", lambda i, choice: Players_To_Test.opposites(choice) if i <= 19 else Players_To_Test.mirror(choice)),
    ("Cooperate First Game (Then Mirror)", lambda i, choice: Players_To_Test.cooperate() if i == 0 else Players_To_Test.mirror(choice)),
]

# Simulate all scenarios
# Simulate all scenarios
for name, strategy in strategies:
    score1, score2 = 0, 0
    for i in range(40):
        player1_choice = Players_To_Test.rand_option()  # Generate Player 1's choice.
        
        # Handle strategies requiring both `i` and `choice`
        if callable(strategy) and name in [
            "Cooperate First Half (Then Mirror)",
            "Cooperate First Half (Then Opposites)",
            "Defect First Half (Then Mirror)",
            "Defect First Half (Then Opposites)",
            "Opposites Every Other",
            "Mirror Every Other",
            "Opposites First Half (Then Mirror)",
            "Cooperate First Game (Then Mirror)",
        ]:
            choice2 = strategy(i, player1_choice)
        elif callable(strategy):
            # Handle strategies requiring only the round index or no arguments
            choice2 = strategy(i) if name in [
                "Cooperate First Half (Then Random)",
                "Cooperate First Half (Then Defect)",
                "Defect First Half (Then Random)",
                "Defect First Half (Then Cooperate)"
            ] else strategy(None)
        else:
            choice2 = strategy  # For fixed strategies like always cooperate/defect.

        # Compute outcomes and update scores
        outcome = prisoners_dilemma(player1_choice, choice2)
        if outcome is not None:  # Ensure valid outcomes before updating scores
            outcome1, outcome2 = outcome
            score1 += outcome1
            score2 += outcome2
    
    # Print the results for the current strategy
    print(f'Random Choice: {score1} {name}: {score2}')

