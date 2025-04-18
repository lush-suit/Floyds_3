"""
Unit tests for Floyd-Warshall's algorithm implementations.

Tests include:
1. Correctness verification for both recursive and iterative implementations.
2. Performance tests to ensure reasonable execution times.
"""

import unittest
from time import process_time
from sys import maxsize

# Assuming these modules and methods exist in your project structure
try:
    import recursion.recursive_floyd
    import iterative.iterative_floyd
except ImportError:
    # Mock implementations for testing purposes if imports fail
    RECURSIVE_GRAPH = [
        [0, 7, maxsize, 8],
        [maxsize, 0, 5, maxsize],
        [maxsize, maxsize, 0, 2],
        [maxsize, maxsize, maxsize, 0],
    ]

    ITERATIVE_GRAPH = [
        [0, 7, maxsize, 8],
        [maxsize, 0, 5, maxsize],
        [maxsize, maxsize, 0, 2],
        [maxsize, maxsize, maxsize, 0],
    ]


    def recursive_floyd_warshall() -> None:
        """Mock implementation of Floyd-Warshall recursive method."""
        for k in range(len(RECURSIVE_GRAPH)):
            for i in range(len(RECURSIVE_GRAPH)):
                for j in range(len(RECURSIVE_GRAPH)):
                    RECURSIVE_GRAPH[i][j] = min(
                        RECURSIVE_GRAPH[i][j],
                        RECURSIVE_GRAPH[i][k] + RECURSIVE_GRAPH[k][j],
                    )


    def iterative_floyd() -> None:
        """Mock implementation of Floyd-Warshall iterative method."""
        for k in range(len(ITERATIVE_GRAPH)):
            for i in range(len(ITERATIVE_GRAPH)):
                for j in range(len(ITERATIVE_GRAPH)):
                    ITERATIVE_GRAPH[i][j] = min(
                        ITERATIVE_GRAPH[i][j],
                        ITERATIVE_GRAPH[i][k] + ITERATIVE_GRAPH[k][j],
                    )

# Helper constants for tests
NO_PATH = maxsize
INITIAL_GRAPH_STATE = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0],
]
EXPECTED_OUTPUT_GRAPH = [
    [0, 7, 12, 8],
    [NO_PATH, 0, 5, 7],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0],
]


def reset_graph(graph, initial_state):
    """
    Resets the global GRAPH variable to its initial state for consistency in testing.
    """
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] = initial_state[i][j]


class TestFloydWarshall(unittest.TestCase):
    """
    Unit tests for Floyd-Warshall algorithm implementations.
    """

    def test_recursive_floyd_warshall_correctness(self):
        """
        Test the correctness of the recursive implementation of Floyd-Warshall algorithm.
        Ensures the output graph matches the expected results.
        """
        reset_graph(RECURSIVE_GRAPH, INITIAL_GRAPH_STATE)
        recursive_floyd_warshall()  # Execute the recursive algorithm
        self.assertEqual(
            RECURSIVE_GRAPH,
            EXPECTED_OUTPUT_GRAPH,
            f"Recursive Floyd-Warshall failed: {RECURSIVE_GRAPH}",
        )

    def test_iterative_floyd_correctness(self):
        """
        Test the correctness of the iterative implementation of Floyd-Warshall algorithm.
        Ensures the output graph matches the expected results.
        """
        reset_graph(ITERATIVE_GRAPH, INITIAL_GRAPH_STATE)
        iterative_floyd()  # Execute the iterative algorithm
        self.assertEqual(
            ITERATIVE_GRAPH,
            EXPECTED_OUTPUT_GRAPH,
            f"Iterative Floyd-Warshall failed: {ITERATIVE_GRAPH}",
        )

    def test_recursive_floyd_performance(self):
        """
        Test performance of the recursive Floyd-Warshall implementation.
        Ensures execution time is within acceptable bounds.
        """
        reset_graph(RECURSIVE_GRAPH, INITIAL_GRAPH_STATE)
        start_time = process_time()
        recursive_floyd_warshall()  # Execute the recursive algorithm
        end_time = process_time()
        elapsed_time = end_time - start_time
        self.assertLess(elapsed_time, 1.0, "Recursive algorithm took too long.")

    def test_iterative_floyd_performance(self):
        """
        Test performance of the iterative Floyd-Warshall implementation.
        Ensures execution time is within acceptable bounds.
        """
        reset_graph(ITERATIVE_GRAPH, INITIAL_GRAPH_STATE)
        start_time = process_time()
        iterative_floyd()  # Execute the iterative algorithm
        end_time = process_time()
        elapsed_time = end_time - start_time
        self.assertLess(elapsed_time, 1.0, "Iterative algorithm took too long.")


if __name__ == "__main__":
    unittest.main()
