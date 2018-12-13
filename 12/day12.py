with open("input12", "r") as f:
    input = f.readlines()
input = [line.strip() for line in input]

plants = input[0]
plants = dict([(key, val) for key, val in enumerate(plants)])
rules = []
for i in range(1, len(input)):
    rules += [input[i].split(" , ")]


def min_plant(state):
    return min([key for key, value in state.items() if value == '#'])


def max_plant(state):
    return max([key for key, value in state.items() if value == '#'])


def extend(state):
    min_ind = min_plant(state)
    max_ind = max_plant(state)
    for i in range(1, 5):
        state[min_ind - i] = "."
        state[max_ind + i] = "."
    return state


def compare(state, ind, rule):
    same = True
    for i in range(5):
        if rule[0][i] != state[ind+i-2]:
            same = False
    if same:
        return rule[1]
    else:
        return False


print(len(plants))
print(plants)

prev_result = 0

for j in range(20):
    indices = [i for i in range(min_plant(plants)-2, max_plant(plants)+3)]
    plants = extend(plants)
    new_plants = {}
    for ind in indices:
        for rule in rules:
            if compare(plants, ind, rule):
                new_plants[ind] = compare(plants, ind, rule)
                break
            else:
                new_plants[ind] = plants[ind]
    plants = new_plants
    print("".join([val for _, val in plants.items()]))
    result = 0
    for key, value in plants.items():
        if value == "#":
            result += key
    print(j, result, result-prev_result)
    prev_result = result

# Part 2: (done by taking the previous j loop to 1001 iterations)
print((50000000000-1001)*62+62717)
