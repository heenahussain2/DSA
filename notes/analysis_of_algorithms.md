## Analysis of Algorithms
The efficiency of algorithms is crucial to avoid impractical run times and excessive memory usage.

### Types of Complexity
- There are 2 types of complexity
    - **Time Complexity**: The time taken by an algorithm to execute in proportion to the size of its input.
    - **Space Complexity**: The amount of the memory used by an algorithm while executing

### Time Complexity
- The basic technique for calculating time complexity is to add up how many basic operations an algorithm will execute.
- The basic operations include assignments, comparisons, arithmetic operations etc.
- Count the number of times each basic operation is executed as a function of size N.
- Add up the counts to get a total number of operations as a function of (N).
- Simplify the total count by:
    - Ignoring constants (e.g., (2N) becomes (N)).
    - Focusing only on the largest term (e.g., ($N^2$ + 40N + 400) simplifies to ($N^2$)).

### Big-O Notation: 
- Used to express the upper bound on the execution time or space requirements of an algorithm.
- It focuses on the most significant term and ignoring constants.