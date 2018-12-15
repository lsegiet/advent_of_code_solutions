data = open("input08").read().strip().split(" ")
data = [int(x) for x in data]


class Node:
	def __init__(self, parent, children_count, metadata_count):
		self.parent = parent
		self.children_count = children_count
		self.children = []
		self.metadata_count = metadata_count
		self.metadata = []
	def get_meta(self):
		if not self.children:
			return sum(self.metadata)
		else:
			meta_children = [self.children[i-1] for i in self.metadata if i > 0 and i <= len(self.children)]
			return sum([child.get_meta() for child in meta_children]) 


sum_meta = 0
parent = Node(None, data[0], data[1])
nodes = [parent]
i = 2
while i < len(data):
	if not parent.children_count and not parent.metadata_count:
		nodes.pop()
		parent = nodes[-1]
	if parent.children_count > 0:
		parent.children_count -= 1

		children_info = data[i]
		i += 1
		meta_info = data[i]
		nodes.append(Node(parent, children_info, meta_info))
		parent.children.append(nodes[-1])
		parent = nodes[-1]

	elif parent.metadata_count > 0:
		parent.metadata_count -= 1
		parent.metadata.append(data[i])
		sum_meta += data[i]
	i += 1
		
print("sum meta:", sum_meta)	
print("get meta:", parent.get_meta())
