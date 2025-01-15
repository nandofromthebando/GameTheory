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