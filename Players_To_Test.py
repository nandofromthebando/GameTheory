import random

# Random model chooses random choice everytime
def rand_option():
    choice = random.choice(["cooperate", "defect"])
    return choice

# Chooses opposites 
def opposites(choice):
    if choice == "cooperate":
        return "defect"
    else:
        return "cooperate"

# Picks the same as the opponent
def mirror(choice):
    if choice == "cooperate":
        return "cooperate"
    else:
        return "defect"   

# Always postive    
def cooperate():
    return "cooperate"

# Always negative
def defect():
    return "defect"