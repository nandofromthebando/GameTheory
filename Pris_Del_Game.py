import matplotlib.pyplot as plt
import Players_To_Test

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

# List of strategies
strategies = [
    ("Always Cooperate", lambda choice: Players_To_Test.cooperate()),
    ("Always Defect", lambda choice: Players_To_Test.defect()),
    ("Opposites", Players_To_Test.opposites),
    ("Mirrored", Players_To_Test.mirror),
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

def plot_results(results):
    """
    Plots the results of the simulation.

    :param results: List of tuples containing strategy names and scores.
    """
    strategies, scores1, scores2 = zip(*results)

    x = range(len(strategies))
    plt.figure(figsize=(12, 6))
    plt.bar(x, scores1, width=0.4, label="Player 1 (Random)", align="center", color="blue")
    plt.bar([p + 0.4 for p in x], scores2, width=0.4, label="Player 2", align="center", color="orange")

    plt.xlabel("Strategies")
    plt.ylabel("Scores")
    plt.title("Prisoner's Dilemma Simulation Results")
    plt.xticks([p + 0.2 for p in x], strategies, rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Run the simulation and collect results
results = []
for name, strategy in strategies:
    score1, score2 = 0, 0
    for i in range(40):
        player1_choice = Players_To_Test.rand_option()

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
            choice2 = strategy(i) if name in [
                "Cooperate First Half (Then Random)",
                "Cooperate First Half (Then Defect)",
                "Defect First Half (Then Random)",
                "Defect First Half (Then Cooperate)",
            ] else strategy(None)
        else:
            choice2 = strategy

        outcome = prisoners_dilemma(player1_choice, choice2)
        if outcome is not None:
            outcome1, outcome2 = outcome
            score1 += outcome1
            score2 += outcome2
    
    results.append((name, score1, score2))

# Plot the results
plot_results(results)
