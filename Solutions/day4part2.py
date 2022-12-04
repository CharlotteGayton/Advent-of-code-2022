input_file = open("Inputs/day4.txt", "r")
data = input_file.read()
data_list = data.split("\n")

total_contain = 0
first_pair = []
second_pair = []
for pair in data_list:
    pair_split = pair.split(",")
    first = pair_split[0].split("-")
    second = pair_split[1].split("-")
    for i in range(int(first[0]),int(first[1])+1):  
        first_pair.append(i)
    for i in range(int(second[0]),int(second[1])+1):  
        second_pair.append(i)
    check_subset_first = any(item in first_pair for item in second_pair)
    check_subset_second = any(item in second_pair for item in first_pair)
    if check_subset_first is True:
        total_contain += 1
    elif check_subset_second is True:
        total_contain += 1
    first_pair = []
    second_pair = []

print(total_contain)
