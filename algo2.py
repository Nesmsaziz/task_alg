class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.edges = []  # List to store all edges

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        """
        A utility function to find the subset of an element i
        """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """
        A function that does union of two subsets
        """
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        """
        Main function to find Minimum Spanning Tree (MST) using Kruskal's algorithm
        """
        # Sort edges based on weight
        self.edges.sort()
        
        mst = []  # To store the resultant MST
        parent = []
        rank = []

        # Create subsets with single elements
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        # Iterate through sorted edges
        for weight, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does not cause a cycle
            if x != y:
                mst.append((u, v, weight))
                self.union(parent, rank, x, y)

        # Print the constructed MST
        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in mst:
            print(f"{u} -- {v} == {weight}")

# Example usage
if __name__ == "__main__":
    g = Graph(4)  # Create a graph with 4 vertices
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal_mst()
