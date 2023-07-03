from MinHeap import MinHeap
from Graph import Graph
from Vertex import Vertex
from Edge import Edge


class OpenVertex(Vertex):

    def get_all_adj(self):
        return [adj for adj in self.edge_pairs]

    def get_edge_cost(self, vert):
        return self.edge_pairs[vert]


class OpenGraph(Graph):

    def get_all_vertices(self):
        return [vert for vert in self._vertices.values()]

    def get_vertex_object(self, vertex_data):
        try:
            vertex = self._vertices[vertex_data]
            return vertex
        except KeyError:
            OpenVertex.push_sort_type(OpenVertex.SortType.DATA)
            new_vertex = OpenVertex(vertex_data)
            self._vertices[vertex_data] = new_vertex
            OpenVertex.pop_sort_type()
            return new_vertex

    def set_graph(self, edges):
        for edge in edges:
            self.add_edge(edge.src.data, edge.dest.data, edge.cost)


class Kruskal:

    def __init__(self, in_graph):
        self._in_graph = in_graph
        self._edge_heap = MinHeap()
        self.build_edge_heap()


    def gen_kruskal(self):
        new_edges = []
        vertex_list = self._in_graph.get_all_vertices()
        vertex_sets = [set([vert]) for vert in vertex_list]
        while len(vertex_sets) > 1:
            try:
                smallest_edge = self._edge_heap.remove()
                src = smallest_edge.src
                dest = smallest_edge.dest
                src_set = self.member_of(src, vertex_sets)
                dest_set = self.member_of(dest, vertex_sets)
                if src_set == dest_set:
                    continue
                vertex_sets[src_set] = \
                    vertex_sets[src_set].union(vertex_sets[dest_set])
                del vertex_sets[dest_set]
                new_edges.append(smallest_edge)
            except MinHeap.EmptyHeapError:
                break
        out_graph = OpenGraph()
        out_graph.set_graph(new_edges)
        return out_graph

    def build_edge_heap(self):
        vertex_list = self._in_graph.get_all_vertices()
        for vertex in vertex_list:
            src = vertex
            dest_list = src.get_all_adj()
            for dest in dest_list:
                self._edge_heap.insert(Edge(src, dest, src.get_edge_cost(dest)))

    @staticmethod
    def member_of(v1, vertex_sets):
        for i, vset in enumerate(vertex_sets):
            if v1 in vset:
                return i


def main():

    my_graph = OpenGraph()
    my_graph.add_edge("v1", "v2", 2)
    my_graph.add_edge("v1", "v4", 1)
    my_graph.add_edge("v2", "v4", 3)
    my_graph.add_edge("v2", "v5", 10)
    my_graph.add_edge("v3", "v1", 4)
    my_graph.add_edge("v3", "v6", 5)
    my_graph.add_edge("v4", "v3", 2)
    my_graph.add_edge("v4", "v5", 2)
    my_graph.add_edge("v4", "v6", 8)
    my_graph.add_edge("v4", "v7", 4)
    my_graph.add_edge("v5", "v7", 6)
    my_graph.add_edge("v7", "v6", 1)

    my_graph.show_adj_table()
    my_kruskal = Kruskal(my_graph)

    my_graph_2 = my_kruskal.gen_kruskal()

    print("ladies and gentlemen, ... I give you kruskal:")

    my_graph_2.show_adj_table()


if __name__ == "__main__":
    main()

r"""  ------- SAMPLE RUN -------
------------------------ 

Adj list for v1: v2(2) v4(1) 
Adj list for v2: v4(3) v5(10) 
Adj list for v4: v3(2) v5(2) v6(8) v7(4) 
Adj list for v5: v7(6) 
Adj list for v3: v1(4) v6(5) 
Adj list for v6: 
Adj list for v7: v6(1) 
ladies and gentlemen, ... I give you kruskal:
------------------------ 

Adj list for v1: v4(1) v2(2) 
Adj list for v4: v5(2) v3(2) v7(4) 
Adj list for v7: v6(1) 
Adj list for v6: 
Adj list for v5: 
Adj list for v2: 
Adj list for v3: 

Process finished with exit code 0

"""