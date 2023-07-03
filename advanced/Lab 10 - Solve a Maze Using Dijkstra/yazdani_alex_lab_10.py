"""
Lab 10: Solve a Maze Using Dijkstra
Alexander Yazdani
CWID: 20399751
Date: 06/26/2023


In this file, a class Graph is defined which uses another class, Vertex to
create objects representing a graph, complete with edges defined in an
adjacency table.  The Dijkstra Algorithm is used within the class to return
the shortest path of vertices between any given start and stop vertices.  The
Graph method Dijkstra_solve() will do so and return a list of the data of
these vertices.
Another class, Maze, is defined which creates a grid of nodes based on the
height and width inputs and sets up vertical and horizontal walls.  The
create_solution_path() method tears down parts of the walls in order to create
a solution path, and then creates dead-end paths to trick the user / algorithm
that is trying to solve the maze.  A solution path is built, and calling
self.solution_path returns a list of nodes representing the solution from
start to finish.  A method create_graph() is defined within the Maze class
which will instantiate a Graph object and create edges for all neighboring
nodes that are not separated by a wall.  Using the dijkstra_solve() method on
this Graph object will return the same list as the Maze objects
self.solution_path property.
During the construction of the maze, 2 different methods (or a combination of
the two) can be used: a random method, a stack method, or a biased combination
of the two.
"""


import time
import random
import collections
from Vertex import Vertex
from collections import deque
from enum import Enum


class Graph:

    def __init__(self):
        self._vertices = {}

    def get_vertex_object(self, vertex_data):
        try:
            vertex = self._vertices[vertex_data]
            return vertex
        except KeyError:
            Vertex.push_sort_type(Vertex.SortType.DATA)
            new_vertex = Vertex(vertex_data)
            self._vertices[vertex_data] = new_vertex
            Vertex.pop_sort_type()
            return new_vertex

    def add_edge(self, src, dest, cost=None):
        src_vertex = self.get_vertex_object(src)
        dest_vertex = self.get_vertex_object(dest)
        src_vertex.add_adj(dest_vertex, cost)

    def show_adj_table(self):
        print("------------------------ \n")
        for vertex in self._vertices:
            self._vertices[vertex].show_adj_list()
            print()

    def clear(self):
        self._vertices = {}

    def dijkstra(self, src):
        Infinity = float("inf")
        src_vertex = self._vertices[src]
        partially_processed = collections.deque()
        for vdata, vobj in self._vertices.items():
            vobj.dist = Infinity
        src_vertex.dist = 0
        partially_processed.append(src_vertex)
        while len(partially_processed) > 0:
            current_vertex = partially_processed.popleft()
            for vobj in current_vertex.edge_pairs:
                if current_vertex.dist + current_vertex.edge_pairs[vobj] < vobj.dist:
                    vobj.dist = current_vertex.dist + current_vertex.edge_pairs[vobj]
                    partially_processed.append(vobj)
                    vobj.prev_in_path = current_vertex

    def show_distance_to(self, src):
        self.dijkstra(src)
        print(f"Distance from {src} to:")
        for vdata, vobj in self._vertices.items():
            print(f"{vdata}: {vobj.dist}")

    def show_shortest_path(self, start, stop):
        start_vert = self._vertices[start]
        stop_vert = self._vertices[stop]
        self.dijkstra(start)
        print(f"Cost of shortest path from {start} to {stop}: {stop_vert.dist}")
        if stop_vert.dist < float("inf"):
            path_stack = collections.deque()
            current_vert = stop_vert
            while current_vert is not start_vert:
                path_stack.append(current_vert)
                current_vert = current_vert.prev_in_path
            print(start_vert.data, end="")
            while len(path_stack) > 0:
                print(f"--->{path_stack.pop().data}", end="")
        print("")
    
    def dijkstra_solve(self, start, stop):
        """
        Uses dijkstra() method to return list of vertex data representing
        shortest path.
        """
        start_vert = self._vertices[start]
        stop_vert = self._vertices[stop]
        self.dijkstra(start)
        if stop_vert.dist < float("inf"):
            path_stack = collections.deque()
            current_vert = stop_vert
            while current_vert is not start_vert:
                path_stack.append(current_vert)
                current_vert = current_vert.prev_in_path
            path = [start_vert.data]
            while len(path_stack) > 0:
                path.append((path_stack.pop()).data)
        return path


class Node:

    class PathState(Enum):
        CLEAR = 0
        VISITED = 1

    def __init__(self):
        self.next_in_solution = None
        self.prev_in_path = None
        self.state = self.PathState.CLEAR


class Maze:

    class NoSolutionGenerated(Exception):
        pass

    class Method(Enum):
        STACK = 0
        RANDOM = 1
        BIAS = 2

    bias_value = .95
    open_char = " "
    h_block_char = "\u2588"
    v_block_char = "\u2588"
    sol_char = "#"

    def __init__(self, width=10, height=10):
        self._h_walls = [[1] * (height - 1) for _ in range(width)]
        self._v_walls = [[1] * height for _ in range(width - 1)]
        self._grid = [[Node() for _ in range(height)] for _ in range(width)]
        self._width = width
        self._height = height
        self._start = None
        self._end = None
        self._solution_path = None

    @property
    def start(self):
        return self._start, 0

    @property
    def end(self):
        return self._end, self._height - 1

    def _build_solution_path(self):
        self._solution_path = [(self._end, self._height - 1)]
        while self._solution_path[-1] != (self._start, 0):
            curr_x, curr_y = self._solution_path[-1]
            next_pos = self._grid[curr_x][curr_y].prev_in_path
            self._solution_path.append(next_pos)
        self._solution_path.reverse()

    @property
    def solution_path(self):
        if not self._solution_path:
            raise Maze.NoSolutionGenerated
        return self._solution_path

    def print_maze(self, with_solution=False):
        top_line = self.h_block_char
        for pos in range(self._width):
            top_line += self.open_char if pos == self._end \
                else self.h_block_char
            top_line += self.h_block_char
        print(top_line)
        for y in range(self._height - 1, -1, -1):

            # Print horizontal walls (except the first time)
            if y < self._height - 1:
                row_line = self.h_block_char
                for x in range(0, self._width):
                    row_line += self.h_block_char if self._h_walls[x][y] \
                        else self.open_char
                    row_line += self.h_block_char
                print(row_line)

            # Print vertical walls and path
            row_line = self.v_block_char
            for x in range(0, self._width):
                if with_solution and (x, y) in self._solution_path:
                    row_line += self.sol_char
                else:
                    row_line += self.open_char
                if x < self._width - 1:
                    row_line += self.v_block_char if self._v_walls[x][y] \
                        else self.open_char
            row_line += self.v_block_char
            print(row_line)
        bot_line = self.h_block_char
        for pos in range(self._width):
            bot_line += self.open_char if pos == self._start \
                else self.h_block_char
            bot_line += self.h_block_char
        print(bot_line)

    def valid_position(self, x, y):
        if x < 0 or x >= self._width or y < 0 or y >= self._height:
            return False
        return True

    def is_wall(self, curr_x, curr_y, prop_x, prop_y):
        if prop_x < curr_x:
            if self._v_walls[prop_x][prop_y]:
                return True
        if curr_x < prop_x:
            if self._v_walls[curr_x][prop_y]:
                return True
        if prop_y < curr_y:
            if self._h_walls[prop_x][prop_y]:
                return True
        if curr_y < prop_y:
            if self._h_walls[prop_x][curr_y]:
                return True
        return False

    def break_wall(self, curr_x, curr_y, prop_x, prop_y):
        if prop_x < curr_x:
            self._v_walls[prop_x][prop_y] = 0
        if curr_x < prop_x:
            self._v_walls[curr_x][prop_y] = 0
        if prop_y < curr_y:
            self._h_walls[prop_x][prop_y] = 0
        if curr_y < prop_y:
            self._h_walls[prop_x][curr_y] = 0

    def create_graph(self):
        """
        Checks every node in Maze and creates an edge for every place a wall
        does not exist.
        """
        maze_graph = Graph()
        for x in range(self._width):
            for y in range(self._height):
                if self.valid_position(x+1, y) and not (self.is_wall(x, y, x+1, y)):
                    maze_graph.add_edge((x, y), (x+1, y), 1)
                if self.valid_position(x, y+1) and not (self.is_wall(x, y, x, y+1)):
                    maze_graph.add_edge((x, y), (x, y+1), 1)
                if self.valid_position(x-1, y) and not (self.is_wall(x, y, x-1, y)):
                    maze_graph.add_edge((x, y), (x-1, y), 1)
                if self.valid_position(x, y-1) and not (self.is_wall(x, y, x, y-1)):
                    maze_graph.add_edge((x, y), (x, y-1), 1)
        return maze_graph

    def create_solution_path(self, method=Method.RANDOM):

        def random_move(curr_pos):
            next_pos = [*curr_pos]
            move = random.randint(0, 3)
            if move == 0:
                next_pos[0] += 1
            elif move == 1:
                next_pos[0] -= 1
            elif move == 2:
                next_pos[1] += 1
            else:
                next_pos[1] -= 1
            return tuple(next_pos)

        def paths_remain(curr_x, curr_y):
            # Top row always has a path
            if curr_y == self._height - 1:
                return True
            for choice in [(curr_x + i, curr_y + j) for i, j in
                           [[-1, 0], [0, -1], [1, 0], [0, 1]]]:
                if choice in unvisited_set:
                    return True
            return False

        self._start = self._width//2
        if method == self.Method.STACK:
            backtrack_stack = deque()
        else:
            backtrack_stack = list()

        backtrack_stack.append((self._start, 0))
        unvisited_set = {(x, y) for x in range(self._width)
                         for y in range(self._height)}
        while True:
            if method == self.Method.RANDOM:
                current_pos = random.choice(backtrack_stack)
                backtrack_stack.remove(current_pos)
            elif method == self.Method.BIAS:
                if random.random() > self.bias_value:
                    current_pos = random.choice(backtrack_stack)
                    backtrack_stack.remove(current_pos)
                else:
                    current_pos = backtrack_stack[-1]
                    backtrack_stack.remove(current_pos)
                    # current_pos = backtrack_stack.pop()
            else:
                current_pos = backtrack_stack.pop()
            # It's possible that this node has been boxed in
            if not paths_remain(*current_pos):
                continue
            unvisited_set.discard(current_pos)
            proposed_next = random_move(current_pos)

            if proposed_next[1] == self._height:
                self._end = current_pos[0]
                self._grid[current_pos[0]][current_pos[1]].next_in_solution = \
                    proposed_next
                break

            if tuple(proposed_next) not in unvisited_set:
                backtrack_stack.append(current_pos)
                continue
            else:
                # We are forging new ground, tear down the wall
                self.break_wall(*current_pos, *proposed_next)
                self._grid[current_pos[0]][current_pos[1]].next_in_solution = \
                    proposed_next
                self._grid[proposed_next[0]][proposed_next[1]].prev_in_path = \
                    current_pos
                if paths_remain(*current_pos):
                    backtrack_stack.append(current_pos)
                backtrack_stack.append(proposed_next)
                unvisited_set.discard(proposed_next)

        # Now fill in the rest of the routes
        while unvisited_set:
            iterable_version = list(unvisited_set)
            for node in iterable_version:
                proposed_next = random_move(node)
                if self.valid_position(*proposed_next) and \
                        proposed_next not in unvisited_set:
                    self.break_wall(*node, *proposed_next)
                    unvisited_set.discard(node)

        self._build_solution_path()


def main():
    my_maze = Maze(10, 10)
    my_maze.create_solution_path()
    my_maze.print_maze()


def create_and_solve():
    for size in [5, 10, 20, 40, 80, 160, 320]:
        print(f"\nMaze Size {size}:")
        for method in Maze.Method:
            d_total_time = 0
            # a_total_time = 0
            trials = 1
            for a in range(trials):
                random.seed(a)
                my_maze = Maze(size, size + 5)
                my_maze.create_solution_path(method=method)
                # Uncomment to print the maze and solution path
                # my_maze.print_maze(True)
                # print()
                d_start = time.perf_counter()
                maze_graph = my_maze.create_graph()
                d_path = maze_graph.dijkstra_solve(my_maze.start, my_maze.end)
                # Uncomment to see the actual and proposed solution paths
                # print(d_path, my_maze.solution_path)
                if d_path != my_maze.solution_path:
                    print("Error: Proposed Dijkstra solution is invalid")
                d_end = time.perf_counter()
                d_total_time += (d_end - d_start)
                # Uncomment for A* graph testing
                # a_start = time.perf_counter()
                # random.seed(a)
                # maze_graph = my_maze.create_graph()
                # a_path = maze_graph.a_star_solve(my_maze.start, my_maze.end)
                # Uncomment to see the actual and proposed solution paths
                # print(d_path, my_maze.solution_path)
                # if a_path != my_maze.solution_path:
                #     print("Error: Proposed A* solution is invalid")
                # a_end = time.perf_counter()
                # a_total_time += (a_end - a_start)
            print(f"Dijkstra took {d_total_time / trials * 1000:.3f} "
                  f"ms with {method}")
            # Uncomment for A* results
            # print(f"A* took {a_total_time / trials * 1000:.3f} "
            #       f"ms with {method}")


if __name__ == "__main__":
    create_and_solve()

"""

Maze Size 5:
Dijkstra took 0.955 ms with Method.STACK
Dijkstra took 0.979 ms with Method.RANDOM
Dijkstra took 0.951 ms with Method.BIAS

Maze Size 10:
Dijkstra took 2.663 ms with Method.STACK
Dijkstra took 3.037 ms with Method.RANDOM
Dijkstra took 2.789 ms with Method.BIAS

Maze Size 20:
Dijkstra took 9.261 ms with Method.STACK
Dijkstra took 9.267 ms with Method.RANDOM
Dijkstra took 8.806 ms with Method.BIAS

Maze Size 40:
Dijkstra took 31.745 ms with Method.STACK
Dijkstra took 34.344 ms with Method.RANDOM
Dijkstra took 33.201 ms with Method.BIAS

Maze Size 80:
Dijkstra took 127.795 ms with Method.STACK
Dijkstra took 129.997 ms with Method.RANDOM
Dijkstra took 124.875 ms with Method.BIAS

Maze Size 160:
Dijkstra took 515.862 ms with Method.STACK
Dijkstra took 498.011 ms with Method.RANDOM
Dijkstra took 503.475 ms with Method.BIAS

Maze Size 320:
Dijkstra took 2030.379 ms with Method.STACK
Dijkstra took 2036.723 ms with Method.RANDOM
Dijkstra took 2018.707 ms with Method.BIAS

"""
