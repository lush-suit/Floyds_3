import sys
from time import process_time  # For timing functions
import tracemalloc  # For memory profiling

# Add directories to a path for importing algorithms
sys.path.append('./')
from src.recursion.recursive_floyd import recursive_floyd_warshall, RECUR_GRAPH
from src.iterative.iterative_floyd import iterative_floyd, ITER_GRAPH

# Initial graph state for testing
INITIAL_GRAPH_STATE = [
    [0, 7, sys.maxsize, 8],
    [sys.maxsize, 0, 5, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, 2],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0],
]


def reset_graph(graph):
    """
    Reset the global GRAPH variable for the algorithm being tested to its initial state.

    :param graph: The graph to reset to the initial state.
    """
    for i, row in enumerate(graph):
        for j, _ in enumerate(row):
            graph[i][j] = INITIAL_GRAPH_STATE[i][j]


def performance_test(function_handle, graph, name):
    """
    Perform a performance test on a given Floyd's algorithm implementation.

    :param function_handle: The function to test. It must accept no parameters.
    :param graph: The graph to use during the test.
    :param name: Name of the algorithm being tested (for logging purposes).
    """
    print(f"{name} Performance Test")

    # Reset the graph before running the function
    reset_graph(graph)

    # Measure memory usage using tracemalloc
    tracemalloc.start()
    
    # Measure start time
    start_time = process_time()

    # Call the function
    function_handle()

    # Measure end time
    end_time = process_time()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    # Print results
    print(f"Execution Time: {elapsed_time:.6f} seconds")
    print(f"Memory Usage: Current = {current / 1024:.2f} KB, Peak = {peak / 1024:.2f} KB")


def test_recursive_floyd():
    """
    Test the recursive version of Floyd's algorithm.

    This function runs the recursive Floyd-Warshall implementation
    using an example graph.
    """
    for i in range(len(RECUR_GRAPH)):
        for j in range(len(RECUR_GRAPH[i])):
            RECUR_GRAPH[i][j] = recursive_floyd_warshall(i, j, len(RECUR_GRAPH) - 1)


if __name__ == "__main__":
    print("Starting performance tests...\n")
    # Test iterative implementation
    performance_test(iterative_floyd, ITER_GRAPH, "Iterative Floyd-Warshall")

    # Test recursive implementation
    performance_test(test_recursive_floyd, RECUR_GRAPH, "Recursive Floyd-Warshall")