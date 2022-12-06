input_file = open("Inputs/day6.txt", "r")
data = input_file.read()
data_list = list(data)

def duplicate_checker(check_numbers):
    remove_duplicates = list(dict.fromkeys(check_numbers))
    # print(remove_duplicates)
    if check_numbers == remove_duplicates: 
        return True
    else: 
        return False


check_numbers = []
counter = 0
for each in data_list:
    check_numbers.append(each)
    counter += 1
    if len(check_numbers) == 4:     
        if duplicate_checker(check_numbers) == False:
            check_numbers = check_numbers[1:]
        else:
            print(counter)