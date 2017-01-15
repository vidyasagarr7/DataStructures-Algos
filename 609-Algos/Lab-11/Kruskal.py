import sys,heapq
from functools import total_ordering

@total_ordering
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.distance == other.distance
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.distance < other.distance
        return NotImplemented

    def __hash__(self):
        return hash(str(self.id))

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def get_edges(self):
        edges = []

        for _vertex in self.vert_dict.values():
            for _con in _vertex.get_connections():
                edges.append((_vertex.get_id(), _con.get_id(), _vertex.get_weight(_con)))
        return edges

    def dfs(self):
        visited = {}
        for _vertex in self.vertices_dict.values():
            if _vertex not in visited:
                self._dfs(_vertex, visited)

    def _dfs(self, vertex, visited_hash):
        visited_hash[vertex] = True
        print('visiting vertex : {}'.format(vertex.get_vertexID()))

        for conn in vertex.get_connections():
            if conn not in visited_hash:
                self._dfs(conn, visited_hash)

parent = dict()
rank = dict()

def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex :
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(v1,v2):
    r1 = find(v1)
    r2 = find(v2)

    if r1 != r2 :
        if rank[r1] > rank[r2] :
            parent[r2] = r1
        else :
            parent[r1]=r2
            if rank[r1] == rank[r2] :
                rank[r2] +=1

def kruskal(graph):
    edges = []
    for _v in graph :
        make_set(_v.get_id())
        for _con in _v.get_connections():
            edges.append((_v.get_weight(_con),_v.get_id(),_con.get_id()))
    edges.sort()

    min_span_tree = set()

    for edge in edges :
        wt, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1,v2)
            min_span_tree.add(edge)
    return min_span_tree

if __name__=='__main__':
    graph = Graph()
    vertices = ['a','b','c','d']
    for _ in vertices :
        graph.add_vertex(_)

    graph.add_edge('a','b',1)
    graph.add_edge('a','c',5)
    graph.add_edge('a','d',3)
    graph.add_edge('b','c',4)
    graph.add_edge('b','d',2)
    graph.add_edge('c','d',1)

    print(kruskal(graph))
