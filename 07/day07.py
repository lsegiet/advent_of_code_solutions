import collections


class Node:

	def __init__(self, index):
		self.index = index
		self.in_nodes = []
		self.marked = False

	def add_in(self, node):
		self.in_nodes.append(node)
		self.in_nodes.sort()

	def __lt__(self, other):
		return self.index < other.index


class Worker:

	def __init__(self, node, start, additional_time = 60):
		self.node = node
		self.start = start
		self.end = ord(node.index) - ord("A") + 1 + start + additional_time


def DFS(list_nodes):
	marked = set()
	result = []
	while len(marked) < len(list_nodes):
		temp = [node for node in list_nodes if node not in marked]
		for node in temp:
			if len([child for child in node.in_nodes if child not in marked]) == 0:
				result.append(node)
				marked.add(node)
				break
	return result

# Parse the input:
data = open("07.in").read().strip().split("\n")
data = [ line.split(" ") for line in data ]
data = [ (line[1], line[7]) for line in data ]

nodes = {}
for (x, y) in data:
	if x not in nodes.keys():
		nodes[x] = Node(x)
	if y not in nodes.keys():
		nodes[y] = Node(y)

	nodes[y].add_in(nodes[x])

# Part 1:
nodes_list = [val for val in nodes.values()]
nodes_list.sort()

order = DFS(nodes_list)
res = [ n.index for n in order ]
print("".join(res))

# Part 2:
num_of_workers = 5
workers = []

time = -1
done = set() # Storing indices of done tasks
started = set() # Storing indices of started task
while(len(done) < len(order)):
	time += 1
	for worker in workers:
		if worker.end == time:
			done.add(worker.node.index)
	workers = [worker for worker in workers if worker.end > time]
	for task in [task for task in order if task.index not in done and task.index not in started]:
		if [pre for pre in task.in_nodes if pre.index in done] == task.in_nodes:
			if  len(workers) < num_of_workers:
				workers.append(Worker(task,time))
				started.add(task.index)
print(time)
