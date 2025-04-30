# README #


### What is this repository for? ###
This project contains implementations of the Floyd-Warshall algorithm 
for finding the shortest paths between all pairs of nodes in a graph. 
It includes both iterative and recursive approaches to solve the problem, 
along with performance testing and unit tests.
Key Features
•	Iterative Floyd-Warshall algorithm: A straightforward implementation using a triple nested loop to compute shortest paths.
•	Recursive Floyd-Warshall algorithm: Explores the problem using recursion, breaking it down into smaller subproblems.
•	Performance Testing: Memory usage and execution time for both implementations are analyzed.
•	Unit Testing: Verifies the correctness and performance of the implementations with test cases.
 
Directory Structure

project/
├── src/
│   ├── iterative/
│   │   └── iterative_floyd.py    # Iterative implementation
│   ├── recursion/
│       └── recursive_floyd.py    # Recursive implementation
├── tests/
│   ├── test_unittests.py         # Unit tests for both algorithms
│   └── performance_test.py       # Performance tests for both algorithms
├── requirements.txt              # Required dependencies
└── README.md                     # Project documentation (this file)
 


### How do I get set up? ###
1. Clone the repository:

    git clone https://github.com/lush-suit/Floyds_3.git
    cd Floyds_3

2. Run the scripts: Navigate to the respective script's directory and run the desired functionality.


### Running the scripts ###

1. Iterative Floyd-Warshall: Execute the iterative algorithm:

   python src/iterative/iterative_floyd.py
2. Recursive Floyd-Warshall: Execute the recursive algorithm:

   python src/recursion/recursive_floyd.py
3. Performance Testing: Run performance tests for both iterative and recursive implementations:

    python tests/performance_test.py

4. Unit Testing: Execute the test suite for correctness and performance:

   python tests/test_unittests.py
 

### Requirements ### 

The following Python libraries are required for this project:
•	pylint: To maintain code quality
•	matplotlib (not directly referenced in code): Useful for potential visualization of graphs in future enhancements.
•	networkx (not directly referenced in code): May be used for handling graphs in larger implementations.
Install these dependencies using the command:

pip install -r requirements.txt

### Contributions ###
Contributions to improve this project are welcome. If you want to contribute:
1.	Fork the repository.
2.	Make your changes in a new branch.
3.	Submit a pull request with a detailed explanation of your changes.
 
### License ###
This project is licensed under the MIT License. See the LICENSE file for more details.
