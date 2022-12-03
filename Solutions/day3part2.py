import string

input_file = open("Inputs/day3.txt", "r")
data = input_file.read()
data_list = data.split("\n")

def matching_letter(current_rucksacks):
    first_array = list(current_rucksacks[0])
    second_array = list(current_rucksacks[1])
    third_array = list(current_rucksacks[2])
    for letter in first_array:
        if letter in second_array:
            if letter in third_array:
                return letter

letter_values = {}
for i in range(27):
    letter_values[string.ascii_lowercase[i-1]]=i
    letter_values[string.ascii_uppercase[i-1]]=i+26

total_value = 0
current_rucksacks = []
for rucksack in data_list:
    current_rucksacks.append(rucksack)
    if len(current_rucksacks) == 3:
        letter = matching_letter(current_rucksacks)
        value = letter_values[letter]
        total_value += value
        current_rucksacks = []



print(total_value)



