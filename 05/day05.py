data = open("input05").read().strip()

Dict = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for c in alphabet:
    Dict[c.lower()] = c.upper()
    Dict[c.upper()] = c.lower()


# Part 1:
def react(data):
    stack = []
    for c in data:
        if stack and c == Dict[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)
    return stack


print(len(react(data)))


# Part 2:
def kill_letter(data, letter):
    stack = []
    for c in data:
        if c.lower() != letter:
            stack.append(c)
    return stack


for c in alphabet:
    temp = kill_letter(data, c)
    print(c, len(react(temp)))
