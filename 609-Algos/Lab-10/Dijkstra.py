
import heapq,sys
from functools import total_ordering

# graph implementation with adjacency lists
@total_ordering
class Vertex:
    def __init__(self,node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbors(self,neighbor,weight=0):
        """

        :param neighbor:
        :param weight:
        :return:
        """
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_vertexID(self):
        return self.id

    def get_weight(self,neighbor):
        return self.adjacent[neighbor]

    def set_distance(self,distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def get_previous(self):
        return self.previous

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

class Graph:
    def __init__(self):
        self.vertices_dict = {}
        self.no_vertices = 0

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def add_vertex(self,node):
        self.no_vertices += 1
        vertex = Vertex(node)
        self.vertices_dict[node] = vertex
        return vertex

    def get_vertex(self,k):
        if k in self.vertices_dict :
            return self.vertices_dict[k]
        else :
            return None

    def add_edge(self,_from,_to, cost=0):
        if _from not in self.vertices_dict :
            self.add_vertex(_from)
        if _to not in self.vertices_dict :
            self.add_vertex(_to)

        self.vertices_dict[_from].add_neighbors(self.vertices_dict[_to],cost)
        self.vertices_dict[_to].add_neighbors(self.vertices_dict[_from],cost)

    def get_vertices(self):
        return self.vertices_dict.keys()

    def set_previous(self,current):
        self.previous = current

    def get_previous(self):
        return self.previous

    def get_edges(self):
        edges = []

        for _vertex in self.vertices_dict.values():
            for _con in _vertex.get_connections():
                edges.append((_vertex.get_vertexID(),_con.get_vertexID(),_vertex.get_weight(_con)))
        return edges

    def dfs(self):
        visited = {}
        for _vertex in self.vertices_dict.values():
            if _vertex not in visited :
                self._dfs(_vertex,visited)

    def _dfs(self,vertex,visited_hash):
        visited_hash[vertex] = True
        print('visiting vertex : {}'.format(vertex.get_vertexID()))

        for conn in vertex.get_connections():
            if conn not in visited_hash :
                self._dfs(conn,visited_hash)

def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def dijkstra(graph,source):

    source.set_distance(0)

    unvisited_queue = [(vertex.get_distance(),vertex) for vertex in graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue) >0 :
        _vert = heapq.heappop(unvisited_queue)
        curr_vertex = _vert[1]
        curr_vertex.set_visited()

        for next in curr_vertex.adjacent:
            if next.visited :
                continue
            dist = curr_vertex.get_distance() + curr_vertex.get_weight(next)
            if dist < next.get_distance() :
                next.set_distance(dist)
                next.set_previous(curr_vertex)
                print('updated current :{} next:{} and new_distance :{}'.format(curr_vertex.get_vertexID,
                                                                                next.get_vertexID,next.get_distance()))
            else :
                print('not updated')

        # empty heap and rebuild it with unvisited items
        while len(unvisited_queue) >0 :
            heapq.heappop(unvisited_queue)

        unvisited_queue = [(_vert.get_distance(),_vert) for _vert in graph if not _vert.visited]
        heapq._heapify_max(unvisited_queue)


if __name__=='__main__':
    graph = Graph()
    string = 'a'
    for i in range(1, 7):
        out = string + str(i)
        graph.add_vertex(out)

    graph.add_edge('a1', 'a2', 4)
    graph.add_edge('a1', 'a3', 1)
    graph.add_edge('a3', 'a2', 2)
    graph.add_edge('a2', 'a5', 4)
    graph.add_edge('a3', 'a4', 4)
    graph.add_edge('a4', 'a5', 4)

    print(graph.get_edges())

    print(graph.dfs())

    print(dijkstra(graph, graph.get_vertex('a1')))

    target = graph.get_vertex('a5')
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : {}'.format(path[::-1]))

