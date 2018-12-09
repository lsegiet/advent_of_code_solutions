with open("input02", "r") as f:
    input = f.readlines()
input = [line.strip() for line in input]


def checksum(twos, threes):
    return twos * threes


# Part 1
twos = 0
threes = 0
wordcount = 1
for line in input:
    dict = {}
    for letter in line:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    add_two = False
    add_three = False
    for key, value in dict.items():
        if value == 2:
            add_two = True
        if value == 3:
            add_three = True
    twos += int(add_two)
    threes += int(add_three)
print(checksum(twos, threes))

# Part 2
for i in range(len(input)):
    for j in range(i, len(input)):
        line_i = input[i]
        line_j = input[j]
        line = ''
        wrong_count = 0
        for ind in range(len(line_i)):
            if line_i[ind] == line_j[ind]:
                line += line_i[ind]
            else:
                wrong_count += 1
        if wrong_count == 1:
            print(line)
