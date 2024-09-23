from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

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
    for node, neighbors in g.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=15, font_weight="bold")

    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    # g.BFS(2)
    g.breadth_first_search(2)

    # Visualize the graph using networkx and matplotlib

    # Display the plot
    plt.show()