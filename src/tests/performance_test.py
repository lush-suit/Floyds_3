"""
This module contains a simple performance test that
compares the recursive version of Floyd's algorithm with the
imperative (iterative) version.
"""

import sys
from time import process_time  # For timing functions

# Add directories to path for importing algorithms
sys.path.append('../')
from recursion.recursive_floyd import recursive_floyd_warshall, GRAPH as recursive_graph
from iterative.iterative_floyd import iterative_floyd, GRAPH as iterative_graph

# Initial graph state for testing
INITIAL_GRAPH_STATE = [
    [0, 7, sys.maxsize, 8],
    [sys.maxsize, 0, 5, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, 2],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0],
]


def performance_test(function_handle, graph):
    """
    Perform a performance test on a given Floyd's algorithm implementation.

    :param function_handle: The function to test. It must accept no parameters.
    :param graph: The graph to use during the test.
    """
    # Reset the graph before running the function
    reset_graph(graph)

    # Measure start time
    start_time = process_time()

    # Call the function
    function_handle()

    # Measure end time
    end_time = process_time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    print(f"Execution Time: {elapsed_time:.6f} seconds")  # Print timings


def reset_graph(graph):
    """
    Reset the global GRAPH variable for the algorithm being tested to its initial state.

    :param graph: The graph to reset to the initial state.
    """
    for i, row in enumerate(graph):
        for j, _ in enumerate(row):
            graph[i][j] = INITIAL_GRAPH_STATE[i][j]


def test_recursive_floyd():
    """
    Test the recursive version of Floyd's algorithm.

    This function runs the recursive Floyd-Warshall implementation
    using an example graph.
    """
    recursive_floyd_warshall(0, 0, 0)


if __name__ == "__main__":
    print("Recursion Test Time")
    performance_test(test_recursive_floyd, recursive_graph)

    print("Iterative Test Time")
    performance_test(iterative_floyd, iterative_graph)
