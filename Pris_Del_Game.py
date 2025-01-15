
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
        return
    
    return outcome[0], outcome[1]
    
# Run the game
print("Prisoner's Dilemma Simulation: Sample size of 40 rounds per scenario")

score1, score2 = 0, 0
for i in range(40):
    outcome1, outcome2 = prisoners_dilemma(Players_To_Test.rand_option(), Players_To_Test.cooperate())
    score1 += outcome1 
    score2 += outcome2
print(f'Random Choice: {score1} Always Cooperate: {score2}')

score1, score2 = 0, 0
for i in range(40):
    outcome1, outcome2 = prisoners_dilemma(Players_To_Test.rand_option(), Players_To_Test.defect())
    score1 += outcome1 
    score2 += outcome2
print(f'Random Choice: {score1} Always Defect: {score2}')

score1, score2 = 0, 0
for i in range(40):
    choice1  = Players_To_Test.rand_option()
    choice2 = Players_To_Test.opposites(choice1)
    outcome1, outcome2 = prisoners_dilemma(choice1, choice2)
    score1 += outcome1 
    score2 += outcome2
print(f'Random Choice: {score1} Opposites: {score2}')

score1, score2 = 0, 0
for i in range(40):
    choice1  = Players_To_Test.rand_option()
    choice2 = Players_To_Test.mirror(choice1)
    outcome1, outcome2 = prisoners_dilemma(choice1, choice2)
    score1 += outcome1 
    score2 += outcome2
print(f'Random Choice: {score1} Mirrored: {score2}')

score1, score2 = 0, 0

for i in range(40):
    if i <= 19:
        outcome1, outcome2 = prisoners_dilemma(Players_To_Test.rand_option(), Players_To_Test.cooperate())
        score1 += outcome1 
        score2 += outcome2
    else: 
        outcome1, outcome2 = prisoners_dilemma(Players_To_Test.rand_option(), Players_To_Test.rand_option())
        score1 += outcome1 
        score2 += outcome2

print(f'Random Choice: {score1} Cooperate First Half (Then Random): {score2}')


for i in range(40):
    if i <= 19:
        outcome1, outcome2 = prisoners_dilemma(Players_To_Test.rand_option(), Players_To_Test.cooperate())
        score1 += outcome1 
        score2 += outcome2
    else: 
        outcome1, outcome2 = prisoners_dilemma(Players_To_Test.rand_option(), Players_To_Test.defect())
        score1 += outcome1 
        score2 += outcome2

print(f'Random Choice: {score1} Cooperate First Half (Then Defect): {score2}')
