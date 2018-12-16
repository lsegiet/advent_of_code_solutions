data = open("16.in").read().strip().split("\n\n")

# Part 1:
data1 = data[:-2]
data1 = [line.split("\n") for line in data1]
data1 = [[line[0].strip("Before:").strip(), line[1], line[2].strip("After:").strip()] for line in data1]
data1 = [[line[0][1:-1], line[1], line[2][1:-1]] for line in data1]
data1 = [[line[0].split(', '), line[1].split(), line[2].split(', ')] for line in data1]
data1 = [[[int(x) for x in subline] for subline in line] for line in data1]

data2 = data[-1]
data2 = data2.split("\n")
data2 = [line.split() for line in data2]
data2 = [[int(x) for x in line] for line in data2]

class Register:
	def __init__(self,array):
		self.opp = array[0]
		self.A = array[1]
		self.B = array[2]
		self.C = array[3]

def opcode(op, reg, instr):
	new_reg= [r for r in reg]
	
	if type(instr) is not Register:
		instr = Register(instr)

	if op == 0:	# addr
		new_reg[instr.C] = reg[instr.A] + reg[instr.B]
	elif op == 1:	# addi
		new_reg[instr.C] = reg[instr.A] + instr.B
	elif op == 2:	# mulr
		new_reg[instr.C] = reg[instr.A] * reg[instr.B]
	elif op == 3:	# muli
		new_reg[instr.C] = reg[instr.A] * instr.B
	elif op == 4:	# banr
		new_reg[instr.C] = reg[instr.A] & reg[instr.B]
	elif op == 5:	# bani
		new_reg[instr.C] = reg[instr.A] & instr.B
	elif op == 6:	# borr
		new_reg[instr.C] = reg[instr.A] | reg[instr.B]
	elif op == 7:	# bori
		new_reg[instr.C] = reg[instr.A] | instr.B
	elif op == 8:	# setr
		new_reg[instr.C] = reg[instr.A]
	elif op == 9:	# seti
		new_reg[instr.C] = instr.A
	elif op == 10:	# gtir
		new_reg[instr.C] = int(instr.A > reg[instr.B])
	elif op == 11:	# gtri
		new_reg[instr.C] = int(reg[instr.A] > instr.B)
	elif op == 12:	# gtrr
		new_reg[instr.C] = int(reg[instr.A] > reg[instr.B])
	elif op == 13:	# eqir
		new_reg[instr.C] = int(instr.A == reg[instr.B])
	elif op == 14:	# eqri
		new_reg[instr.C] = int(reg[instr.A] == instr.B)
	elif op == 15:	# eqrr
		new_reg[instr.C] = int(reg[instr.A] == reg[instr.B])
	return new_reg


# possible operation_mapping for a certain opcode
posso = { j : set(i for i  in range(16)) for j in range(16)} 

num_of_misbehaved = 0
for [before, instr, after] in data1:
	diff = 0
	for i in range(16):
		if opcode(i, before, instr) == after:
			diff += 1
		else:
			if i in posso[instr[0]]:
				posso[instr[0]].remove(i)
	if diff >= 3:
		num_of_misbehaved += 1
print(num_of_misbehaved)

taken_operations = set()
operation_mapping = {}
while sum([len(posso[i]) for i in posso.keys()]) > 0:

	# check if number has only one possible operation:
	for num in posso.keys():
		if len(posso[num]) == 1:
			operation_mapping[num] = posso[num].pop()
			taken_operations.add(operation_mapping[num])
	# check if operation is possible for only one number
	for op in range(16):
		count = 0
		for key, val in posso.items():
			if op in val:
				count+=1
				the_only_key = key
		if count == 1:
			posso[the_only_key] = set()
			operation_mapping[the_only_key] = op
			taken_operations.add(op)

	for op in taken_operations:
		for num in posso.keys():
			if op in posso[num]:
				posso[num].remove(op)
	

# Part 2:
reg = [0 for _ in range(4)] 		# starting program
for d in data2:
	reg = opcode(operation_mapping[d[0]],reg,d)
print(reg[0])
