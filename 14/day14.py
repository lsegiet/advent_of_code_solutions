# Part 1:
recipes = [3, 7]
elf1 = 0
elf2 = 1

num_of_recipes = 990941 + 10
num_of_recipes = 9 + 10

while(len(recipes) < num_of_recipes):
	new_recipe = recipes[elf1] + recipes[elf2]
	if new_recipe >= 10:
		recipes.append(1)
	recipes.append(new_recipe % 10)
	elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
	elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

result_part_1 = [str(x) for x in recipes[num_of_recipes-10:num_of_recipes]]
print("".join(result_part_1))


# Part 2:
recipes = [3, 7]
elf1 = 0
elf2 = 1

seq = 990941
sequence = [int(x) for x in str(seq)]

found_sequence = False
while(not found_sequence):
	new_recipe = recipes[elf1] + recipes[elf2]
	if new_recipe >= 10:
		recipes.append(1)
		if recipes[-len(sequence):] == sequence:
			result_part_2 = len(recipes)-len(sequence)
			found_sequence = True
	recipes.append(new_recipe % 10)
	if recipes[-len(sequence):] == sequence:
		result_part_2 = len(recipes)-len(sequence)
		found_sequence = True
	elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
	elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

print(result_part_2)
