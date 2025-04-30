"""
This module contains a **proper recursive implementation** of Floyd's Algorithm.
It calculates the shortest paths between all pairs of nodes and prints the initial
and final graph matrices.
"""

from sys import maxsize

# Constants
NO_PATH: int = maxsize
RECUR_GRAPH: list[list[int]] = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0],
]
MAX_LENGTH = len(RECUR_GRAPH[0])
NO_PATH_MARKER = "No Path"


def main():
    """Calling function for the recursive Floyd-Warshall algorithm."""
    print("Initial Graph Matrix:")
    print_graph_matrix(RECUR_GRAPH)

    # Start the recursive algorithm for all pairs and all levels of k
    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            RECUR_GRAPH[i][j] = recursive_floyd_warshall(i, j, MAX_LENGTH - 1)

    print("\nFinal Graph Matrix:")
    print_graph_matrix(RECUR_GRAPH)

    print("\nDetailed Distances Between Nodes:")
    print_out_graph()


def print_out_graph():
    """
    This function prints out the graph with distances
    and a placeholder for nodes with no path.
    """
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            distance = RECUR_GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER

            print(f"Distance from Node {start_node} to Node {end_node} is {distance}")


def print_graph_matrix(matrix: list[list[int]]) -> None:
    """
    Prints the adjacency matrix of the graph.
    Unreachable paths are replaced with `NO_PATH_MARKER`.
    """
    for row in matrix:
        formatted_row = [
            (NO_PATH_MARKER if value == NO_PATH else value) for value in row
        ]
        print(formatted_row)


def recursive_floyd_warshall(i: int, j: int, k: int) -> int:
    """
    Proper recursive implementation of Floyd-Warshall.
    Computes the shortest path from i to j using intermediate nodes up to k.

    :param i: Start node
    :param j: End node
    :param k: Intermediate nodes to consider (from 0 to k)
    :return: Shortest path distance from i to j considering intermediates up to k
    """
    # Base case: no intermediate nodes to consider (k = 0)
    if k < 0:
        return RECUR_GRAPH[i][j]

    # Recursive case: find the shortest path considering the current intermediate node
    direct_path = recursive_floyd_warshall(i, j, k - 1)
    if NO_PATH in (RECUR_GRAPH[i][k], RECUR_GRAPH[k][j]):
        path_with_intermediate = NO_PATH
    else:
        path_with_intermediate = (
                recursive_floyd_warshall(i, k, k - 1) + recursive_floyd_warshall(k, j, k - 1)
        )

    return min(direct_path, path_with_intermediate)


if __name__ == "__main__":
    main()


def floyd_warshall():
    """Placeholder function for the Floyd-Warshall algorithm."""
    return None
