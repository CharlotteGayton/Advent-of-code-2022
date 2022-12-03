import string

input_file = open("Inputs/day3.txt", "r")
data = input_file.read()
data_list = data.split("\n")

def matching_letter(first_compartment, second_compartment):
    first_array = list(first_compartment)
    second_array = list(second_compartment)
    for letter in first_array:
        if letter in second_array:
            return letter

letter_values = {}
for i in range(27):
    letter_values[string.ascii_lowercase[i-1]]=i
    letter_values[string.ascii_uppercase[i-1]]=i+26

total_value = 0
for rucksack in data_list:
    rucksack_array = list(rucksack)
    first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    shared_letter = matching_letter(first_compartment, second_compartment)
    value = letter_values[shared_letter]
    total_value += value

print(total_value)