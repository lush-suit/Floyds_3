"""
Floyd's Algorithm Implementation

This module implements a simple version of Floyd's algorithm for computing the
shortest paths in a graph. It contains these main functions:
- main: Controls the execution of the script.
- print_out_graph: Outputs the graph with node distances.
- iterative_floyd: Computes the shortest path.
- print_graph_matrix: Prints the graph matrix.

Global variables:
- NO_PATH: Marker for no paths (set to sys.maxsize).
- ITER_GRAPH: Adjacency matrix containing distances between nodes.
- MAX_LENGTH: Graph dimension.
- NO_PATH_MARKER: Placeholder for unreachable paths in the output.
"""

from itertools import product
from sys import maxsize

# Constants
NO_PATH: int = maxsize
ITER_GRAPH: list[list[int]] = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0],
]
MAX_LENGTH: int = len(ITER_GRAPH[0])
NO_PATH_MARKER: str = "No Path"


def main() -> None:
    """
    Execute Floyd's Algorithm using an iterative approach and display the results.
    """
    print("Initial Graph Matrix:")
    print_graph_matrix(ITER_GRAPH)

    iterative_floyd()

    print("\nFinal Graph Matrix:")
    print_graph_matrix(ITER_GRAPH)

    print("\nDetailed Distances Between Nodes:")
    print_out_graph()


def print_out_graph() -> None:
    """
    Prints out the graph distances with
    a placeholder for unreachable paths.
    """
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            distance = ITER_GRAPH[start_node][end_node]
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


def iterative_floyd() -> None:
    """
    Compute the shortest paths for all pairs of nodes using Floyd's algorithm.
    """
    for intermediate, start_node, end_node in product(
            range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)
    ):
        if start_node == end_node:
            ITER_GRAPH[start_node][end_node] = 0
            continue

        ITER_GRAPH[start_node][end_node] = min(
            ITER_GRAPH[start_node][end_node],
            ITER_GRAPH[start_node][intermediate] + ITER_GRAPH[intermediate][end_node],
        )


if __name__ == "__main__":
    main()
