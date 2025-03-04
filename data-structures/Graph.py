from collections import defaultdict, deque
import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(g):
    G = nx.Graph()

    # Add edges to the NetworkX graph based on our custom graph structure
    for node, neighbors in g.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=15, font_weight="bold")

    # Visualize the graph using networkx and matplotlib
    # Display the plot
    plt.show()


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    # Function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def get_graph(self):
        return self.graph

    def set_graph(self, g):
        self.graph = g

    def add_node(self, u):
        self.graph[u] = {}

    def add_weighted_edge(self, u, v, w, directed=False):

        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        if u in self.graph and v in self.graph:
            self.graph[u][v] = w  # u, v connected by edge with weight w

        if not directed:
            self.graph[v][u] = w  # add edge to opposite direction

    def __str__(self):
        return str(self.graph)

    def myBreadthFirstSearch(self):
        size = len(self.graph)
        visited = [False] * size
        queue = [0]  # assume start note is 0

        while queue:
            print('queue: ', queue)
            v = queue.pop(0)
            visited[v] = True
            print('neighbors: ', self.graph[v])
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    queue.append(neighbor) # append the neighbours to the q is not visited


    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    # find the s
    def breadth_first_search(self, s):
        for item in self.graph[s]:
            print(item, end="\t")

    def initiate_from_file(self):
        file = open("input.txt", "r")
        # Read the entire content of the file
        print('type: ', type(file))
        first_line = file.readline().strip()
        nodes, directed = first_line.split()
        print('nodes: ', nodes, 'directed: ', directed)
        g = Graph()
        # initialize the graph
        for node in range(0, int(nodes)):
            g.add_node(node)
        print('nodes: ', g)
        for line in file:
            print(line.strip())  # .strip() to remove newline characters
            line_info = line.split()
            g.add_weighted_edge(int(line_info[0]), int(line_info[1]), int(line_info[2]), directed)
        # Print the content
        # Close the file
        file.close()
        return g

    def calculate_degree(self, graph_instance):
        degree_array = [0] * len(graph_instance.get_graph())
        for node in range(1, len(graph_instance.get_graph()) + 1):
            degree_array[node-1] = (len(graph_instance.get_graph()[node]))
        return degree_array

    # def sort_by_degree(self, graph_instance):
    #     # find the nodes of the max degree



# Driver code
if __name__ == '__main__':
    # Create a graph given in
    # the above diagram
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 6)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(5, 9)
    g.add_edge(5, 15)

    G = nx.Graph()

    # Add edges to the NetworkX graph based on our custom graph structure
    # for node, neighbors in g.graph.items():
    #     for neighbor in neighbors:
    #         G.add_edge(node, neighbor)
    #
    # # Draw the graph
    # pos = nx.spring_layout(G)
    # nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=15, font_weight="bold")
    #
    # print("Following is Breadth First Traversal"
    #       " (starting from vertex 2)")
    # # g.BFS(2)
    # g.breadth_first_search(2)
    #
    # # Visualize the graph using networkx and matplotlib
    #
    # # Display the plot
    # plt.show()
    graph = g.initiate_from_file()
    print('graph: ', graph)
    g.set_graph(graph.get_graph())
    # degree = g.calculate_degree(graph)
    # print('degree: ', degree)
    g.myBreadthFirstSearch()
