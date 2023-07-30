"""
<Matthew Mazzaccaro>
"""

# could be useful for Dijkstra
from queue import PriorityQueue

# for timing checks
import time

# use a very large number as placeholder for infinity
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


def printAdjMat(mat, width=3):
    """ Print an adj/weight matrix padded with spaces and with vertex names. """
    res_str = '     ' + ' '.join([str(v).rjust(width, ' ') for v in range(len(mat))]) + '\n'
    res_str += '    ' + '-' * ((width + 1) * len(mat)) + '\n'
    for i, row in enumerate(mat):
        row_str = [str(elem).rjust(width, ' ') if elem < INF else ' 999' for elem in row]
        res_str += ' ' + str(i).rjust(2, ' ') + ' |' + ' '.join(row_str) + "\n"
    print(res_str)


def dijkstra_w_pri_queue(W, sv):
    """ Dijkstra's algorithm using a priority queue. """
    D = [INF] * len(W)
    D[sv] = 0
    pq = PriorityQueue()
    pq.put((0, sv))

    while not pq.empty():
        curr_distance, curr_vertex = pq.get()
        if curr_distance > D[curr_vertex]:
            continue
        for vertex, weight in enumerate(W[curr_vertex]):
            if weight != INF:
                new_distance = D[curr_vertex] + weight
                if new_distance < D[vertex]:
                    D[vertex] = new_distance
                    pq.put((new_distance, vertex))

    return D


def assign03_main():
    """ Demonstrate the functions, starting with creating the graph. """
    g = adjMatFromFile("py_vs_X_assign3.txt")

    # Run Dijkstra's using a pri queue for a single starting vertex, v2
    start_vert = 2
    start_time = time.time()
    res_dijkstra_pri_queue = dijkstra_w_pri_queue(g, start_vert)
    elapsed_time_dijkstra_pri_queue = time.time() - start_time
    print(f"  Dijkstra's w/ pri queue elapsed time (single starts): {elapsed_time_dijkstra_pri_queue:.2f}")

# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign03_main()
