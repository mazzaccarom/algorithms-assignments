"""
Assign 04 - <Matt Mazzaccaro>

Directions:
    * Complete the graph algorithm functions given below. Note that it may be
      helpful to define auxiliary/helper functions that are called from the
      functions below.  Refer to the README.md file for additional info.

    * NOTE: As with other assignments, please feel free to share ideas with
      others and to reference sources from textbooks or online. However, be sure
      to **cite your resources in your code. Also, do your best to attain a
      reasonable grasp of the algorithm that you are implementing as there will
      very likely be questions related to it on quizzes/exams.

    * NOTE: Remember to add a docstring for each function, and that a reasonable
      coding style is followed (e.g. blank lines between functions).
      Your program will not pass the tests if this is not done!
"""
# co-pilot and ChatGPT-4 were used to help generate the code for this assignment

# for timing checks
import time

import sys
INF = sys.maxsize


def adjMatFromFile(filename):
    """ Create an adj/weight matrix from a file with verts, neighbors, and weights. """
    f = open(filename, "r")
    n_verts = int(f.readline())
    print(f" n_verts = {n_verts}")
    adjmat = [[INF] * n_verts for i in range(n_verts)]
    for i in range(n_verts):
        adjmat[i][i] = 0
    for line in f:
        int_list = [int(i) for i in line.split()]
        vert = int_list.pop(0)
        assert len(int_list) % 2 == 0
        n_neighbors = len(int_list) // 2
        neighbors = [int_list[n] for n in range(0, len(int_list), 2)]
        distances = [int_list[d] for d in range(1, len(int_list), 2)]
        for i in range(n_neighbors):
            adjmat[vert][neighbors[i]] = distances[i]
    f.close()
    return adjmat


def prims(W):
    """ Prim's algorithm for finding the minimum spanning tree of a graph. """
    n = len(W)
    mst, mst_verts = [], [0]

    while len(mst_verts) < n:
        min_weight, next_vert, next_edge = INF, None, None
        for v in mst_verts:
            for i in range(n):
                if W[v][i] != INF and i not in mst_verts and W[v][i] < min_weight:
                    min_weight, next_vert, next_edge = W[v][i], i, (v, i, W[v][i])
        mst_verts.append(next_vert)
        mst.append(next_edge)

    return mst


def kruskals(W):
    """ Kruskal's algorithm for finding the minimum spanning tree of a graph. """
    def find_parent(parent, i):
        if parent[i] == i:
            return i
        return find_parent(parent, parent[i])

    n = len(W)
    edges = [(i, j, W[i][j]) for i in range(n) for j in range(i + 1, n) if W[i][j] != INF]
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    mst = []

    for edge in edges:
        set_u, set_v = find_parent(parent, edge[0]), find_parent(parent, edge[1])
        if set_u != set_v:
            mst.append(edge)
            parent[set_v] = set_u

    return mst


def assign04_main():
    """ Demonstrate the functions, starting with creating the graph. """
    g = adjMatFromFile("graph_verts100_B.txt")

    # Run Prim's algorithm
    start_time = time.time()
    res_prim = prims(g)
    elapsed_time_prim = time.time() - start_time
    print(f"Prim's runtime: {elapsed_time_prim:.2f}")

    # Run Kruskal's for a single starting vertex, 2
    start_time = time.time()
    res_kruskal = kruskals(g)
    elapsed_time_kruskal = time.time() - start_time
    print(f"Kruskal's runtime: {elapsed_time_kruskal:.2f}")

    # Check that sum of edges weights are the same for this graph
    cost_prim = sum([e[2] for e in res_prim])
    print("MST cost w/ Prim: ", cost_prim)
    cost_kruskal = sum([e[2] for e in res_kruskal])
    print("MST cost w/ Kruskal: ", cost_kruskal)
    assert cost_prim == cost_kruskal


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign04_main()