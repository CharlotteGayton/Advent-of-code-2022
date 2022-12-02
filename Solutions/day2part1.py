input_file = open("Inputs/day2.txt", "r")
data = input_file.read()
data_list = data.split("\n")

rock = 1
paper = 2
scissors = 3

lose = 0
draw = 3
win = 6

def hierarchy_score(choice, current_score):
    if choice == 'X':
        current_score += rock
    elif choice == 'Y':
        current_score += paper
    else: 
        current_score += scissors
    return current_score


def game_score(opponent, choice, current_score):
    if opponent == 'A':
        if choice == 'X':
            current_score += draw
        if choice == 'Y':
            current_score += win
    if opponent == 'B':
        if choice == 'Y':
            current_score += draw
        if choice == 'Z':
            current_score += win
    if opponent == 'C':
        if choice == 'Z':
            current_score += draw
        if choice == 'X':
            current_score += win
    return current_score

current_score = 0
total_score = 0
for each_game in data_list: 
    play = each_game.split(" ")
    opponent = play[0]
    choice = play[1]
    
    current_score = hierarchy_score(choice, current_score)
    current_score = game_score(opponent, choice, current_score)
    
    total_score += current_score
    current_score = 0

print(total_score)