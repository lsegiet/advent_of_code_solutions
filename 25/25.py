def dist(X, Y):
    return sum([abs(x-y) for x, y in zip(X,Y)])


class Graph:
    def __init__(self, filename):
        data = open(filename).read().strip().split("\n")
        self.nodes = set(tuple(int(x) for x in line.split(",")) for line in data)
        self.edges = { v : [w for w in self.nodes if v != w and dist(v, w) <= 3]  for v in self.nodes }
        self.not_visited = { v for v in self.nodes }


    def Count_components(self):
        count = 0
        while self.not_visited:
            vert = self.not_visited.pop()
            self.DFS(vert)
            count += 1
        return count

    def DFS(self, start_node):
        Queue = [start_node]
        while Queue:
            current = Queue.pop()
            for i in self.edges[current]:
                if i in self.not_visited:
                    Queue.append(i)
                    self.not_visited.remove(i)
        return True
        

filename = "25.in"
G = Graph(filename)
print(G.Count_components())
