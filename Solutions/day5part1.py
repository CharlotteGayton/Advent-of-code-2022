input_file = open("Inputs/day5.txt", "r")
data = input_file.read()
data_list = data.split("\n")
actions = data_list[10:]

map_of_lanes = []

for each in [1,5,9,13,17,21,25,29,33]:
    current = []
    for i in reversed(range(9)):
        if data_list[i][each] != ' ':
            current.append(data_list[i][each])
    map_of_lanes.append(current)

for each in actions:
    command = each.split(' ')
    for j in range(int(command[1])):
        from_lane = int(command[3])-1
        moving_value = map_of_lanes[from_lane][-1]
        map_of_lanes[from_lane] = map_of_lanes[from_lane][:-1]
        map_of_lanes[int(command[5])-1].append(moving_value)

final = []
for each in map_of_lanes:
    final.append(each[-1])
final = ''.join(final)
print(final)


