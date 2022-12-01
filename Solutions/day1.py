input_file = open("Inputs\day1.txt", "r")
data = input_file.read()
data_list = data.split("\n")
data_list.append('')

current_elf = 0
largest_calorie_elf = 0
second_calorie_elf = 0
third_calorie_elf = 0

for snack in data_list:
    if snack == '':
        if current_elf > largest_calorie_elf:
            third_calorie_elf = second_calorie_elf
            second_calorie_elf = largest_calorie_elf
            largest_calorie_elf = current_elf
        elif current_elf > second_calorie_elf:
            third_calorie_elf = second_calorie_elf
            second_calorie_elf = current_elf
        elif current_elf > third_calorie_elf:
            third_calorie_elf = current_elf
        current_elf = 0
    else:
        snack_value = int(snack)
        current_elf += snack_value

sum_of_top_three = largest_calorie_elf + second_calorie_elf + third_calorie_elf
print(sum_of_top_three)