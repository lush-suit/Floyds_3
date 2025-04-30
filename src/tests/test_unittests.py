import sys
import unittest
import time  # For performance measurement

sys.path.append('./')
from src.iterative.iterative_floyd import ITER_GRAPH, iterative_floyd, NO_PATH
from src.recursion.recursive_floyd import RECUR_GRAPH, recursive_floyd_warshall, MAX_LENGTH


class TestFloydAlgorithm(unittest.TestCase):

    def setUp(self):
        # Expected result graph for correctness verification
        self.expected_graph = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0],
        ]

    def test_iterative_floyd(self):
        # Test correctness of the iterative approach
        iterative_floyd()
        self.assertEqual(ITER_GRAPH, self.expected_graph)

    def test_recursive_floyd(self):
        # Test correctness of the recursive approach
        for i in range(MAX_LENGTH):
            for j in range(MAX_LENGTH):
                RECUR_GRAPH[i][j] = recursive_floyd_warshall(i, j, MAX_LENGTH - 1)

        self.assertEqual(RECUR_GRAPH, self.expected_graph)

    def test_iterative_performance(self):
        # Test performance of iterative Floyd-Warshall with larger input
        start_time = time.perf_counter()

        # Example: simulate running iterative Floyd on a larger dataset (if supported)
        iterative_floyd()

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Iterative Floyd-Warshall Performance Test Completed in {elapsed_time:.5f} seconds")
        self.assertTrue(elapsed_time < 5, "Iterative Floyd-Warshall took too long")

    def test_recursive_performance(self):
        # Test performance of recursive Floyd-Warshall with larger input
        start_time = time.perf_counter()

        # Example: simulate running recursive Floyd on a larger dataset (if supported)
        for i in range(MAX_LENGTH):
            for j in range(MAX_LENGTH):
                RECUR_GRAPH[i][j] = recursive_floyd_warshall(i, j, MAX_LENGTH - 1)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Recursive Floyd-Warshall Performance Test Completed in {elapsed_time:.5f} seconds")
        self.assertTrue(elapsed_time < 5, "Recursive Floyd-Warshall took too long")


if __name__ == "__main__":
    unittest.main()
