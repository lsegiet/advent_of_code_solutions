import re


with open("input03", "r") as f:
    input = f.readlines()
input = [line.strip() for line in input]

max_width = 0
max_height = 0
elves = []
for line in input:
    numbers = re.findall("-?\d+", line)
    numbers = [int(x) for x in numbers]
    [id, x, y, width, height] = numbers
    if x + width > max_width:
        max_width = x+width
    if y + height > max_height:
        max_height = y + height
    elves += [numbers]

# Part 1:
table = [[0 for i in range(max_height)] for j in range(max_width)]
count = 0

for elf in elves:
    [id, x, y, width, height] = elf
    for i in range(width):
        for j in range(height):
            if table[x+i][y+j] == 0:
                table[x+i][y+j] = id
            elif table[x+i][y+j] > 0:
                table[x+i][y+j] = -1
                count += 1
print(count)
