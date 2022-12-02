input_file = open("Inputs/day2.txt", "r")
data = input_file.read()
data_list = data.split("\n")

rock = 1
paper = 2
scissors = 3

rock_values = {'X': scissors, 'Y': rock, 'Z': paper}
paper_values = {'X': rock, 'Y': paper, 'Z': scissors}
scissors_values = {'X': paper, 'Y': scissors, 'Z': rock}

def round(opponent, choice, current_score):
    if opponent == 'A':
        current_score += rock_values.get(choice)
    if opponent == 'B':
        current_score += paper_values.get(choice)
    if opponent == 'C':
        current_score += scissors_values.get(choice)
    return current_score

def converter(choice, current_score):
    if choice == 'Y':
        current_score += 3
    if choice == 'Z':
        current_score += 6
    return current_score


current_score = 0
total_score = 0
for each_game in data_list: 
    play = each_game.split(" ")
    opponent = play[0]
    choice = play[1]
    
    current_score = round(opponent, choice, current_score)
    current_score = converter(choice, current_score)
    
    total_score += current_score
    current_score = 0

print(total_score)